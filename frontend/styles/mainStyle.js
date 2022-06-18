import { StyleSheet } from "react-native";
import { COLORS, BORDER, FONTS } from "./common";

const main = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: COLORS.primaryFG
    },

    response: {
        alignItems: 'center',
        justifyContent: 'center'
    }
})

const header = StyleSheet.create({
    container: {
        backgroundColor: COLORS.nav,
        width:'auto',
        padding:5,
    },
    
    title: {
        fontSize:25,
        fontStyle:FONTS.primary,
        color:'white',
        textAlign:'center'
    }
})

const introduction = StyleSheet.create({
    container: {
        backgroundColor: COLORS.primary,
        padding:1,
        margin:1,

        borderWidth: BORDER.borderWidth,
        borderColor: BORDER.borderColor,
        borderRadius: BORDER.borderRadius,
        width:'90%',
        alignSelf:"center",
        textAlign:'center'
    },
    head :{
        fontSize: 23,
        fontWeight: 'bold',
        textAlign:'center'
    },
    body: {
        fontSize: 15
    }
})

const questionInput = StyleSheet.create({
    container: {
        backgroundColor: COLORS.secondary,
        padding: 1,
        margin: 1,

        borderWidth: BORDER.borderWidth,
        borderColor: BORDER.borderColor,
        borderRadius: BORDER.borderRadius,
        
        flexDirection: "row",
        alignSelf:"center",
        width:'90%'
    },

    input: {
        backgroundColor: COLORS.primaryFG,
        textAlign: 'center',
        padding: 1,
        flex:2,
    },

    button: {
        backgroundColor: COLORS.primary,
        padding: 1,
        margin: 1,
        flex:1,
        textAlign:'center'
    }
})

const response = StyleSheet.create({
    container: {
        flex: 1,
        alignSelf: 'center',
        backgroundColor: COLORS.primary,
        width:'90%'
    },

    table: {
        margin:2,
    },

    row: {
        height:'auto',
        width:'auto',
        flexDirection:'row'
    },

    itemHeader: {
        backgroundColor: COLORS.primary,
        flex: 1,
        height: 'auto',
        
        borderWidth: BORDER.borderWidth,
        borderColor: BORDER.borderColor,
        borderRadius: BORDER.borderRadius,
    },

    tableBorder: {
        borderWidth: BORDER.borderWidth,
        borderColor: BORDER.borderColor
    },

    headTxt: {
        fontSize: 18,
        fontWeight: 'bold'
    },

    rowTxt: {
        margin: 6,
        color: 'black',
        fontSize:15,
        flex:1
    }
})
export { main, questionInput, response, header, introduction}