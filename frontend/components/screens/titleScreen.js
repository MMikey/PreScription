import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity, FlatList } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { main, response, questionInput } from '../../styles/mainStyle'

class TitleScreen extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nlQuery: '',
      results: []
    }
  }

  static navigationOptions = {
    header: null
  }

  componentDidMount() {
    this.showQuestions()
  }

  showQuestions = async () => {
    const value = await AsyncStorage.getItem('@session_token')

    return fetch('http://localhost:8000/api/question', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + value,
      }
    })
      .then((response) => {
        if (response.status === 200){
          return response.json()
        } else if (response.status === 401){
          this.props.navigation.navigate('Login')
        }
      })
      .then((responseJson) => {
        this.setState({
          results: responseJson
        })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  postQuestion = async () => {

    return fetch('http://localhost:8000/api/question/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 'utterance': this.state.nlQuery })
    })
      .then((response) => {
        if (response.status === 401) {
          this.props.navigation('Login')
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }



  render() {
    return (
      <View style={main.container}>
        <View style={questionInput.container}>
          <TextInput
            placeholder='Question'
            style={questionInput.input}
            onChangeText={(nlQuery) => this.setState({ nlQuery })}
            onSubmitEditing={() => this.postQuestion()}
            value={this.state.nlQuery}
          />
        </View>
        <View style={response.container}>
          <View style={response.row}>
            <Text style={response.itemHeader}>
              Question
            </Text>
            <Text style={response.itemHeader}>
              Translated SQL
            </Text>
          </View>
          <FlatList
            ListEmptyComponent={<Text style={response.item}>No questions to display</Text>}
            data={this.state.results}
            renderItem={({ item }) => (
              <View style={response.row}>
                <Text style={response.item}>
                  {item.utterance}
                </Text>
                <Text style={response.item}>
                  {item.sql_query}
                </Text>
              </View>
            )}
          />
        </View>
      </View>
    )
  }
}

export default TitleScreen