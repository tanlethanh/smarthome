import { Text, View } from "react-native";
import React, { Component } from "react";
import { SafeAreaView } from "react-native-safe-area-context";

export function LoginScreen() {
    return (
        <SafeAreaView>
            <View className="flex flex-col h-screen w-screen items-center justify-center">
                <Text className="text-3xl">LoginScreen</Text>
            </View>
        </SafeAreaView>
    );
}

export default LoginScreen;
