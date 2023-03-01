from Adafruit_IO import Client, MQTTClient, Data
from adafruit_interface import IAdafruit


class AdafruitWrapper(IAdafruit):

    def __init__(self, username, api_key):
        super().__init__()
        self.username = username
        self.api_key = api_key
        self.rest_client: Client | None = None
        self.mqtt_client: MQTTClient | None = None
        self.init_client()
        self.start_mqtt()

    def init_client(self):
        self.rest_client = Client(self.username, self.api_key)
        self.mqtt_client = MQTTClient(self.username, self.api_key)

    def set_up_mqtt_client(self):
        def connected(client):
            # Connected function will be called when the client is connected to Adafruit IO.
            # This is a good place to subscribe to feed changes.  The client parameter
            # passed to this function is the Adafruit IO MQTT client so you can make
            # calls against it easily.
            print('Connected to Adafruit IO')

        def subscribe(client, userdata, mid, granted_qos):
            # This method is called when the client subscribes to a new feed.
            print('Subscribed to {0} with QoS {1}'.format(mid, granted_qos[0]))

        def disconnected(client):
            # Disconnected function will be called when the client disconnects.
            print('Disconnected from Adafruit IO!')

        def message(client, feed_id, payload):
            # Message function will be called when a subscribed feed has a new value.
            # The feed_id parameter identifies the feed, and the payload parameter has
            # the new value.
            print('Feed {0} received new value: {1}'.format(feed_id, payload))

        self.mqtt_client.on_connect = connected
        self.mqtt_client.on_disconnect = disconnected
        self.mqtt_client.on_message = message
        self.mqtt_client.on_subscribe = subscribe

    def start_mqtt(self):
        self.mqtt_client.connect()
        self.mqtt_client.loop_background()

    def create_feed(self, feed):
        self.rest_client.create_feed(feed)

    def get_feed(self, feed):
        return self.rest_client.feeds(feed)

    def get_all_feeds(self):
        return self.rest_client.feeds()

    def delete_feed(self, feed):
        return self.rest_client.delete_feed(feed)

    def send_data_to_feed(self, feed, data):
        return self.rest_client.send_data(feed, data)

    def send_list_data_to_feed(self, feed, data_list: Data):
        return self.rest_client.send_batch_data(feed, data_list)

    def get_last_data(self, feed):
        return self.rest_client.receive(feed)

    def subscribe_feed(self, feed_id):
        return self.mqtt_client.subscribe(feed_id)

    def unsubscribe_feed(self, feed_id):
        return self.mqtt_client.unsubscribe(feed_id=feed_id)
