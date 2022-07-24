import React, { Component } from 'react'
import { View, Text } from 'react-native'

import { header } from '../../styles/mainStyle'

class Header extends Component {
  constructor (props) {
    super(props)
  }


  render () {
    return (
      <View style={header.container}>
          <Text style={header.title}>PreScription: A Natural Language Interface to a Database</Text>
      </View>
    )
  }
}

export default Header