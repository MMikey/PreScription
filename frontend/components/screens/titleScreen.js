import React, { Component } from 'react'
import { Text, View, TextInput, ScrollView } from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage'

import { main, response, questionInput, introduction } from '../../styles/mainStyle'

import Header from '../shared/header'
import Info from '../shared/info'
import { Container, Table, Button, Alert, Card } from 'react-bootstrap'
import { StyleSheet } from "react-native";



class TitleScreen extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nlQuery: '',
      results: [],
      sqlresults: [],
      tableHeaders: [],
      error: false,
      errorMsg: 'Please Enter A Natural Language Query to get started'
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
        if ('error' in responseJSON) {
          throw new Error(responseJSON['error'])
        }
        this.setState({
          sqlresults: responseJSON
        })
        console.log(this.state['sqlresults'])
        this.setState({
          tableHeaders: Object.keys(this.state['sqlresults'][0])
        })

      })
      .catch((err) => {
        this.setState({
          errorMsg: err.message,
          error: true
        })
        console.log(this.state.errorMsg)
      })
  }


  postQuestion = async () => {
    this.setState({
      errorMsg: '',
      error: false
    })

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
        this.setState({
          results: responseJSON
        })
        this.processQuery(responseJSON.id)
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
        <Card border='light' className='text-center m-2'>
          <Card.Body>

            <Card.Title> Welcome!</Card.Title>
            <Info />
            <Card.Text>
              Enter a Natural Language Query to Begin
            </Card.Text>
    

          <View style={questionInput.container}>
            <TextInput
              placeholder='Natural Language Question'
              style={questionInput.input}
              onChangeText={(nlQuery) => this.setState({ nlQuery })}
              value={this.state.nlQuery}
              />
            <Button
              onClick={() => this.postQuestion()}
              variant='primary'
              >Enter</Button>
          </View>
        </Card.Body>
        </Card>

        <ScrollView style={response.container}>
          {(this.state['results'].length == 0 || (this.state.error == true))
            ?
            <View style={response.empty}>
              <Alert variant='warning'>
                {this.state.errorMsg}
              </Alert>
            </View>
            :
            <Table striped bordered hover>
              <thead>
                <tr>
                  {this.state.tableHeaders.map((data, index) => (
                    <th>{data}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {
                  this.getTableData(this.state.sqlresults).map((rowData, rowIndex) => (
                    <tr>
                      {rowData.map((data, columnInd) => (
                        <td key={columnInd}>{data}</td>
                      ))}
                    </tr>
                  ))
                }
              </tbody>

            </Table>
          }
        </ScrollView>

      </View>
    )
  }
}

export default TitleScreen