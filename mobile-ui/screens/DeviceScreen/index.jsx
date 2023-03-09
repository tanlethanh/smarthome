import FanScreen from "./Fan";
import AirConditionerScreen from "./AirConditioner";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import TabBar from './TabBar'

const DeviceTab = createBottomTabNavigator();

function DeviceScreen({ navigator }) {
    return (
        <DeviceTab.Navigator
            initialRouteName="fan"
            screenOptions={{
                headerShown: false
            }}
            tabBar={(props) => <TabBar {...props} />}
        >
            <DeviceTab.Screen
                name="Air conditioner"
                component={AirConditionerScreen}
            ></DeviceTab.Screen>
            <DeviceTab.Screen
                name="Fan"
                component={FanScreen}
            ></DeviceTab.Screen>
            <DeviceTab.Screen
                name="Light 2"
                component={FanScreen}
            ></DeviceTab.Screen>
            <DeviceTab.Screen
                name="Light 1"
                component={FanScreen}
            ></DeviceTab.Screen>
            <DeviceTab.Screen
                name="Machine"
                component={FanScreen}
            ></DeviceTab.Screen>
        </DeviceTab.Navigator>
    );
}

export { DeviceScreen };
