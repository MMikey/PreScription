import React, { Component } from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'


import TitleScreen from './components/screens/titleScreen'
import HistoryScreen from './components/screens/historyScreen'

import Ionicons from 'react-native-vector-icons/Ionicons';
import 'bootstrap/dist/css/bootstrap.css';

const Tab = createBottomTabNavigator()

class App extends Component {
  render () {
    return (
      // Tab Navigator points to stack navigator in navigation folder
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={({ route }) => ({
            tabBarIcon: ({ focused, color, size }) => {
              let iconName;
  
              if (route.name === 'Home') {
                iconName = focused
                  ? 'information-circle'
                  : 'information-circle-outline';
              } else if (route.name === 'History') {
                iconName = focused ? 'library' : 'library-outline';
              }
  
              // You can return any component that you like here!
              return <Ionicons name={iconName} size={size} color={color} />;
            },
            tabBarActiveTintColor: 'tomato',
            tabBarInactiveTintColor: 'gray',
            headerShown: false
          })}
        >
          <Tab.Screen name='Home' component={TitleScreen} />
          <Tab.Screen name='History' component={HistoryScreen} />
        </Tab.Navigator>
      </NavigationContainer>
    )
  }
}

export default App