import React, { Component, useState } from 'react'
import { Text } from 'react-native'
import Alert from 'react-bootstrap/Alert'
import Button from 'react-bootstrap/Button'

class Info extends Component {
    constructor(props) {
        super(props)
        this.state = {
            show: true
        }
    }

    render() {
        if (this.state['show']) {
            return (
               
                    <Alert 
                    show={this.state['show']} 
                    variant="success" 
                    onClose={() => this.setState({show:false})}
                    dismissible
                    >
                        <Alert.Heading>Current questions available</Alert.Heading>
                        <p>
                            "Which patients are currently admitted?"{"\n"}
                            "Which staff are currently working?"{"\n"}
                            "Show me a list of all patients"{"\n"}
                            "Show me a list of all staff"{"\n"}
                            "Show me a list of all treatments"{"\n"}
                        </p>
                    </Alert>
               
            )
        }
        return (<Button onClick={() => this.setState({ show: true })}>Show
            available queries</Button>)
    }
}

export default Info