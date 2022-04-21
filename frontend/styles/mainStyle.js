import { StyleSheet } from "react-native";
import { COLORS, BORDER } from "./common";

const main = StyleSheet.create({
    container:{
        flex:1,
        backgroundColor:COLORS.primaryBG
    },

    response:{
        alignItems:'center',
        justifyContent:'center'
    }
})

const questionInput = StyleSheet.create({
    container : {
        backgroundColor:COLORS.container,
        alignSelf:'center',
        padding: 1,
        margin:6,
        width:'90%',
        borderWidth:BORDER.borderWidth,
        borderColor:BORDER.borderColor,
        borderRadius:BORDER.borderRadius,
    },

    input : {
        backgroundColor:COLORS.container,
        alignSelf:'center',
        textAlign:'center',
        padding: 1,
        margin:6,
        width:'70%',
        height:'90%',
    }
})

const response = StyleSheet.create({
    container : {
        flex:1,
        alignContent: 'center',
        padding:5,
        backgroundColor: COLORS.primaryBG
    },

    row : {
      flexDirection:'row',
      backgroundColor: COLORS.secondary
    },

    item : {
        backgroundColor:COLORS.secondaryContainerBG,
        flex:1,
        minWidth:'40%', 
        fontSize:20,
        padding:5,
        margin:5,

        borderWidth:BORDER.borderWidth,
        borderColor:BORDER.borderColor,
        borderRadius:BORDER.borderRadius,

        elevation: 10,
        shadowColor:'#EFEFEF',
        shadowRadius:10
    },

    itemHeader: {
        backgroundColor:COLORS.container,
        flex:1,
        minWidth:'40%', 
        fontSize:25,
        padding:5,
        margin:5,
        textAlign:'center',

        borderWidth:BORDER.borderWidth,
        borderColor:BORDER.borderColor,
        borderRadius:BORDER.borderRadius,
    },

    text : {
        fontSize:15,
        fontWeight:'bold' 
    }
})
export { main, questionInput, response }