import { TextInput } from "react-native";

function Input({ placeholder, value, setValue, secureTextEntry = false, className }) {
    return (
        <TextInput
            placeholder={placeholder ? placeholder : "Input text"}
            className="p-5 rounded-xl text-lg bg-white"
            secureTextEntry={secureTextEntry}
        ></TextInput>
    );
}

export { Input };
