import { StyleSheet } from "react-native";
import { COLORS } from "./common";

const main = StyleSheet.create({
    container:{
        flex:1
    },

    response:{
        alignItems:'center',
        justifyContent:'center'
    }
})

const questionInput = StyleSheet.create({
    container : {
        alignSelf:'center',
        padding: 5
    },

    input : {
        fontSize:15,
        alignSelf:'center',
        minWidth:'80%'
    }
})

const response = StyleSheet.create({
    container : {
        flex:1,
        alignContent: 'center',
        padding:5,
        backgroundColor: COLORS.container
    },

    tableBorder : {
        borderWidth: 1, 
        borderColor: '#ffa1d2'
    },

    tableHeader : {
        backgroundColor: COLORS.secondary,
        flex:1,
        minWidth:'40%', 
        fontSize:20,
        padding:5,
        margin:5,
        borderWidth:5,
        borderColor:COLORS.secondary,
        color:COLORS.button,
        borderRadius:5
    },

    row : {
      flexDirection:'row'
    },

    item : {
        flex:1,
        minWidth:'40%', 
        fontSize:20,
        padding:5,
        margin:5,
        borderWidth:5,
        borderColor:COLORS.secondary,
        borderRadius:5
    },

    text : {
        fontSize:15,
        fontWeight:'bold' 
    }
})
export { main, questionInput, response }