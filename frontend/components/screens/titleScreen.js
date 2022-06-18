import React, { Component } from 'react'
import { Text, View, TextInput, TouchableOpacity, ScrollView, TouchableHighlightBase } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { Table, Row } from 'react-native-table-component'
import { main, response, questionInput, introduction } from '../../styles/mainStyle'

import Header from '../shared/header'
import { StyleSheet } from "react-native";

import { Moment } from 'moment'


class TitleScreen extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nlQuery: '',
      results: [],
      sqlresults: [],
      tableHeaders: []
    }
  }

  static navigationOptions = {
    header: null
  }

  processQuery = async (id) => {
    return fetch('http://localhost:8000/api/question/' + id + '/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        if (response.status === 200) {
          return response.json()
        } else {
          throw new Error('error')
        }
      })
      .then((responseJSON) => {
        this.setState({
          sqlresults: responseJSON
        })
        console.log(this.state['sqlresults'])
        this.setState({
          tableHeaders: Object.keys(this.state['sqlresults'][0])
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
        if (response.status === 200) {
          return response.json()
        } else {
          console.log('error')
        }
      })
      .then((responseJSON) => {
        this.setState({ //basically you can do all 
          results: responseJSON
        })
        this.processQuery(responseJSON.id)
        console.log(responseJSON.id)
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
      for (let j = 0; j < row.length; j++) {
        if (typeof row[j] === 'boolean') {
          row[j] = String(row[j])
        }
      }
      tableData.push(row)
    }

    return tableData
  }



  render() {
    return (
      <View style={main.container}>
        <Header></Header>
        <View style={introduction.container}>
          <Text style={introduction.head}>Welcome!</Text>
            <Text style={introduction.body}>
              To start you can ask questions about patients, staff and treatments. Current questions available:{"\n"}
              "Which patients are currently admitted?"{"\n"}
              "Which staff are currently working?"{"\n"}
              "Show me a list of all patients"{"\n"}
              "Show me a list of all staff"{"\n"}
              "Show me a list of all treatments"{"\n"}
              To Get started, please input a natural language question below.</Text>
        </View>

        <View style={questionInput.container}>
          <TextInput
            placeholder='Question'
            style={questionInput.input}
            onChangeText={(nlQuery) => this.setState({ nlQuery })}
            value={this.state.nlQuery}
          />
          <TouchableOpacity
            onPress={() => this.postQuestion()}
            style={questionInput.button}>
            <Text>Enter</Text>
          </TouchableOpacity>
        </View>

        <View style={response.container}>
          <ScrollView bounces={false}>

            <Table
              style={StyleSheet.flatten(response.container)}
            >
              <Row
                data={this.state.tableHeaders}
                style={StyleSheet.flatten(response.itemHeader)}
                textStyle={StyleSheet.flatten(response.headTxt)}
              />

              {
                this.getTableData(this.state.sqlresults).map((rowData, index) => (
                  <Row
                    data={rowData}
                    style={[StyleSheet.flatten(response.row), index % 2 && { backgroundColor: '#F7F6E7' }]}
                  />
                ))
              }

            </Table>

          </ScrollView>
        </View>

      </View>
    )
  }
}

export default TitleScreen