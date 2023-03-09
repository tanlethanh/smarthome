import { DeviceLayout } from "../../layouts";
import { AirConditioner } from "../../components";

function AirConditionerScreen() {
    return (
        <DeviceLayout deviceName={"Air conditioner"}>
            <AirConditioner></AirConditioner>
        </DeviceLayout>
    );
}

export default AirConditionerScreen