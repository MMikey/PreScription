import React, { Component } from 'react'
import { View, Button, Text } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { header } from '../../styles/mainStyle'

class Header extends Component {
  constructor (props) {
    super(props)

    this.state = {
      token: ''
    }
  }


  render () {
    return (
      <View style={header.container}>
          <Text style={header.title}>An Untitled Natural Language Interface to a Database</Text>
      </View>
    )
  }
}

export default Header