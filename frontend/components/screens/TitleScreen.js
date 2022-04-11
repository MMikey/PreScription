import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity } from 'react-native'
import AsyncStorage from '@react-native-async-store'


class TitleScreen extends Component {
  constructor (props) {
    super(props)

    this.state = {
      nlQuestion : '',
      results: []
    }
  }

  static navigationOptions = {
    header: null
  }

  showQuestions= async () => {
      
    return window.fetch('http://localhost:8000/api', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then((response) => {
      this.setState({ results: response.data })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  postQuestion = async () => {

    return window.fetch('http://localhost:8000/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.state.nlQuestion)
    })
    .then((response) => {
      this.showQuestions()
    })
  }

  render () {
    return (
      <View>

      </View>
    )
  }
}

export default TitleScreen