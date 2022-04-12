import React, { Component } from 'react'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import TitleScreen from '../components/screens/titleScreen'

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
      </HomeStack.Navigator>
    )
  }
}

export default HomeStackScreen