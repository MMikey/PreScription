import React, { Component } from 'react'
import { View, Button } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

class Header extends Component {
  constructor (props) {
    super(props)

    this.state = {
      token: ''
    }
  }

  componentDidMount () {
    this._unsubscribe = this.props.navigation.addListener('focus', () => {
      this.checkLoggedIn()
    })
  }

  componentWillUnmount () {
    this._unsubscribe()
  }

  checkLoggedIn = async () => {
    const value = await AsyncStorage.getItem('@session_token')
    if (value !== null) {
      this.setState({ token: value })
    } else {
      this.props.navigation.navigate('Login')
    }
  }

  render () {
    return (
      <View>
          
      </View>
    )
  }
}

export default Header