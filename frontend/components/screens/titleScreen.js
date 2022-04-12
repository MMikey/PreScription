import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity, FlatList } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'


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
      body: JSON.stringify(this.state.nlQuery)
    })
      .then((response) => {
        this.showQuestions()
      })
  }



  render() {
    return (
      <View>
        <TextInput
          placeholder='Question'
          onChangeText={(nlQuery) => this.setState({ nlQuery })}
          onSubmitEditing={() => this.postQuestion()}
          ListEmptyComponent={<Text>No questions to display</Text>}
          value={this.state.nlQuery}
        />
        <FlatList
          data={this.state.results}
          renderItem={({ item }) => (
            <View> <Text>{item.sql_statement}</Text> </View>
          )}
        />
      </View>
    )
  }
}

export default TitleScreen