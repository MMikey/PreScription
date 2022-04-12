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
      body: JSON.stringify({'nl_question':this.state.nlQuery})
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
      <View>
        <TextInput
          placeholder='Question'
          onChangeText={(nlQuery) => this.setState({ nlQuery })}
          onSubmitEditing={() => this.postQuestion()}
          value={this.state.nlQuery}
        />
        <FlatList
          ListEmptyComponent={<Text>No questions to display</Text>}
          data={this.state.results}
          renderItem={({ item }) => (
            <Text>{item.nl_question}</Text> 
          )}
        />
      </View>
    )
  }
}

export default TitleScreen