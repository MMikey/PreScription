import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity, FlatList } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { main, response, questionInput } from '../../styles/mainStyle'
import { Touchable } from 'react-native-web'

class LoginScreen extends Component {
    constructor(props) {
        super(props)

        this.state = {
            username: '',
            password: ''
        }
    }

    static navigationOptions = {
        header: null
    }

    login = async () => {
        return window.fetch('http://localhost:8000/api-token-auth/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state)
        })
            .then((response) => {
                return response.json()
            })
            .then(async (responseJson) => {
                await AsyncStorage.setItem('@session_token', responseJson.token)
                this.props.navigation.navigate('Title')
            })
            .catch((error) => {
                console.log(error)
            })
    }

    render() {
        return (
            <View style={main.container}>
                <TextInput
                    placeholder='enter username...'
                    style={questionInput.input}
                    onChangeText={(username) => this.setState({ username })}
                    value={this.state.username}
                />
                <TextInput
                    placeholder='enter password...'
                    style={questionInput.input}
                    onChangeText={(password) => this.setState({ password })}
                    value={this.state.password}
                    secureTextEntry
                />

                <TouchableOpacity
                onPress={() => this.login()}>
                    <Text>Login</Text>
                </TouchableOpacity>
            </View>
        )
    }
}

export default LoginScreen