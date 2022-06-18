import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity, FlatList, ScrollView} from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { StyleSheet } from 'react-native'
import { main, response, questionInput } from '../../styles/mainStyle'

import Header from '../shared/header'

import { Table, Row } from 'react-native-table-component'
import Moment from 'moment'

class HistoryScreen extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nlQuery: '',
      results: [],
      tableHeaders: ['Natural Language Question', 'SQL', 'Date Posted']
    }
  }

  static navigationOptions = {
    header: null
  }

  componentDidMount() {
    this.showQuestions()
  }

  deleteQuestions = async (id) => {
    return fetch('http://localhost:8000/api/question/' + id, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      }
    })
    .then((response) => {
      if ((response.status) === 200){
        return response.json()
      } else {
        throw new Error('oops something went wrong!')
      }
    })
    .catch((error) => {
      console.log(error)
    })
  }

  showQuestions = async () => {
    return fetch('http://localhost:8000/api/question/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
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

  getTableData = (results) => {
    let tableData = []

    for (let i = 0; i < results.length; i++) {
      let item = results[i]
      let row = Object.values(item)
      tableData.push(row)
    }

    return tableData
  }

  render() {
    return (
      <View style={main.container}>
        <Header></Header>

        <ScrollView style={response.container}>
          
        <Table style={StyleSheet.flatten(response.container)}>

              <Row
                data={this.state.tableHeaders}
                style={StyleSheet.flatten(response.itemHeader)}
                textStyle={StyleSheet.flatten(response.headTxt)}
              />

              {
                this.getTableData(this.state.results).map((rowData, index) => (
                    <Row
                      data={rowData.splice(1)}
                      style={[StyleSheet.flatten(response.row), index % 2 && { backgroundColor: '#F7F6E7' }]}
                    />
                ))
              }

            </Table>
        </ScrollView>
        
      </View>
    )
  }
}

export default HistoryScreen