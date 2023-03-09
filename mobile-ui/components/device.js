import { View, Text, Button, StyleSheet } from "react-native";
import { StatusBar } from "expo-status-bar";
import { SafeAreaView } from "react-native-safe-area-context";
import Lamp from "./Lamp";
import Fan from "./Fan";
function Device({ navigation , device}) {
    if (device == "Fan"){
        return <Fan powerState={false}></Fan>
    }
    else if (device =="Lamp") {
        return (
            <Lamp powerState={false}></Lamp>
        )

    }
}

export default Device ;
