import time, queue, serial, threading
from serial.serialutil import SerialException
import serial.tools.list_ports as serialtool

# Gateway Configurations
GATEWAY_ID = "GTW002"
GROUP_KEY = "iot-lab"
PUB_QOS = 1
SUB_QOS = 1
STAT_TOPIC = "gateway-status"
SUBSCRIBE_TOPICS = [
    "arduino-led",  # record led status
    "arduino-servo",  # record change in servo angle
    STAT_TOPIC  # listen to disconnect signal from the broker
]
SCAN_DELAY = 1.0
TIME_OUT = 5.0  # maximum waiting time for blocking
MAX_FAILED_ATTEMPTS = 3

# Devices Configurations
BAUDRATE = 9600  # Arduino default baudrate
COM_TOKEN = 'USB Serial Device'


# ----------------------------------- COLOR CODES ------------------------------------
class col:
    cdtag = '\033[35;1m'
    mestag = '\033[1;34m'
    pubtag = '\033[31;1m'
    subtag = '\033[0;33m'
    good = '\033[92m'
    bad = '\033[31m'
    user = '\033[0;95m'
    topic = '\033[0;30m'
    message = '\033[0;94m'
    stage = '\033[0;93m'
    esc = '\033[0m'


# --------------------------------- GLOBAL VARIABLES ---------------------------------
block = False  # flag to block thread
exquit = False  # flag to raise disconnect interrupt
greeting = True  # flag to indicate whether this is the first time we connect
reinit = False  # flag to call init() procedure on reconnect
texceed = False  # flag to indicate we've reached maximum blocking time
failcount = 0  # count attempts on fail activity
msg = ''  # hold buffer message read from serial

# ---------------------------------- SHARED-MEMORY -----------------------------------
messageBuffer = queue.Queue()  # holds incoming messages
devicesBuffer = queue.Queue()  # holds outgoing messages
terminate = False  # control thread termination
scanning = False  # flag to indicate initial setup
timerexit = False  # control timer termination


# --------------------------------- UTILITY FUNCTIONS ---------------------------------
def getport():
    ports = serialtool.comports()
    target = ''
    for p in ports:
        strport = str(p)
        if COM_TOKEN in strport:
            target = strport.split(" ")[0]
    if target == '':
        print(f"{col.bad}[WARNING]{col.esc} no COM port found")
    else:
        print(f"Attached to: {target}")
    return target


# data is in the form "!<num>:<topic>:<value>#"
def dispatch(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    sdata = data.split(":")
    if scanning: devicesBuffer.join()
    devicesBuffer.put((sdata[1], sdata[2]))


# this routine will be constantly called to read any serial data
def driver():
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        global msg
        msg = msg + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in msg) and ("!" in msg):
            begin = msg.find("!")
            end = msg.find("#")
            dispatch(msg[begin: end + 1])
            if end == len(msg):
                msg = ''
            else:
                msg = msg[end + 1:]


# the co-routine to scan for incoming serial data
def watcher():
    global exquit, ser
    while True:
        if terminate:
            ser.close()
            break
        try:
            driver()
        except SerialException:
            print(f"{col.bad}[WARNING]{col.esc} Lost connection to serial. Quitting...")
            ser.close()
            exquit = True
            break


# the co-routine to time the waiting
def timer():
    global texceed
    count = 0
    while True:
        if timerexit:
            break
        time.sleep(1.0)
        count = count + 1
        if count == TIME_OUT:
            texceed = True
            break


# ------------------------------- MAIN GATEWAY SCRIPT --------------------------------
# connect to serial com port
# -----
try:
    print(f"{col.stage}Finding serial port...{col.esc}")
    ser = serial.Serial(getport(), BAUDRATE)
except SerialException:
    print("Quitting...")
    exit(1)

# start external thread
# -----
taskWatching = threading.Thread(target=watcher)
taskWatching.start()

gateway = AdafruitWrapper()
