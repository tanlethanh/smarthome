import { View, Text } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

function DeviceLayout({ children }) {
    return (
        <SafeAreaView>
            <View>
                {children}
                <Text>Device layout footer</Text>
            </View>
        </SafeAreaView>
    );
}

export { DeviceLayout };
