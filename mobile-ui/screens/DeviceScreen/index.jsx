import FanScreen from "./Fan";
import AirConditionerScreen from "./AirConditioner";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

const DeviceTab = createBottomTabNavigator();

function DeviceScreen({ navigator }) {
    return (
        <DeviceTab.Navigator initialRouteName="fan">
            <DeviceTab.Screen
                name="air-conditioner"
                component={AirConditionerScreen}
            ></DeviceTab.Screen>
            <DeviceTab.Screen
                name="fan"
                component={FanScreen}
            ></DeviceTab.Screen>
        </DeviceTab.Navigator>
    );
}

export { DeviceScreen };
