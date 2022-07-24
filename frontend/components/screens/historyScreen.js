import React, { Component } from 'react'
import { View, ScrollView } from 'react-native'

import { main, response } from '../../styles/mainStyle'

import Header from '../shared/header'

import { Button, Table } from 'react-bootstrap'

import Moment from 'moment'

import { useFocusEffect } from '@react-navigation/native'

class HistoryScreen extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nlQuery: '',
      results: [],
      tableHeaders: ['ID', 'Natural Language Question', 'SQL', 'Date Posted']
    }
  }

  static navigationOptions = {
    header: null
  }

  componentDidMount() {
    this.showQuestions()
    this.props.navigation.addListener('willFocus', this.showQuestions())
  }


  deleteQuestions = async (id) => {
    return fetch('http://localhost:8000/api/question/' + id, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      }
    })
      .then((response) => {
        if ((response.status) === 200) {
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
        if (response.status === 200) {
          return response.json()
        } else if (response.status === 401) {
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
     
      Moment.locale('en')
      row[row.length-1] = Moment(row[row.length-1]).format('d MMM hh:mm')
      tableData.push(row)
    }
    return tableData
  }

  render() {
    return (
      <View style={main.container}>
        <Header></Header>

        <ScrollView style={response.container}>

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
                this.getTableData(this.state.results).map((rowData, index) => (
                  <tr>
                    {rowData.map((data,columnInd) => (
                          <td>{data}</td>
                        ))}
                  </tr>
                ))
              }

            </tbody>
          </Table>
          <div className='align-items-center'>
            <Button onClick={() => this.deleteQuestions()} variant='danger'> Delete All</Button>
          </div>
        </ScrollView>

      </View>
    )
  }
}

export default HistoryScreen