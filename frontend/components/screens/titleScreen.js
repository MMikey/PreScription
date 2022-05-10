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
    
    return fetch('http://localhost:8000/api/questions', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        return response.json()
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

    return fetch('http://localhost:8000/api/questions/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 'nl_question': this.state.nlQuery })
    })
      .then((response) => {
        console.log(JSON.stringify(this.state))
        this.showQuestions()
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
                  {item.nl_question}
                </Text>
                <Text style={response.item}>
                  {item.translated_statement}
                  </Text>
                <Text style={response.item}>
                  {item.sql_statement}
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