import { DeviceLayout } from "../../layouts";
import { Fan } from "../../components";
import { Text } from 'react-native'

export default function FanScreen() {
    return (
        <DeviceLayout deviceName="Fan Device">
            <Fan></Fan>
        </DeviceLayout>
    );
}
