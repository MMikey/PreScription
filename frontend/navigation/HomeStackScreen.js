import React, { Component } from 'react'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import TitleScreen from '../components/screens/titleScreen'
import LoginScreen from '../components/screens/loginScreen'

const HomeStack = createNativeStackNavigator()

class HomeStackScreen extends Component {
  render () {
    return (
      <HomeStack.Navigator
        screenOptions={{
          headerShown: false
        }}
      >
        <HomeStack.Screen name='Title' component={TitleScreen} />
        <HomeStack.Screen name='Login' component={LoginScreen} />
      </HomeStack.Navigator>
    )
  }
}

export default HomeStackScreen