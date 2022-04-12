import React, { Component } from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

import HomeStackScreen from './navigation/HomeStackScreen'

const Tab = createBottomTabNavigator()

class App extends Component {
  render () {
    return (
      // Tab Navigator points to stack navigator in navigation folder
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={{
            headerShown: false
          }}
        >
          <Tab.Screen name='Home' component={HomeStackScreen} />
        </Tab.Navigator>
      </NavigationContainer>
    )
  }
}

export default App