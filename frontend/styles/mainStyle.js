import { StyleSheet } from "react-native";
import { COLORS, BORDER, FONTS } from "./common";

const main = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: COLORS.primaryBG
    },

    response: {
        alignItems: 'center',
        justifyContent: 'center'
    }
})

const header = StyleSheet.create({
    container: {
        backgroundColor: COLORS.primary,
        width:'auto',
        padding:5,
    },
    
    title: {
        fontSize:25,
        fontStyle:FONTS.primary,
        color:'white',
        marginLeft:1,
    }
})

const introduction = StyleSheet.create({
    container: {
        alignSelf:"center",
        textAlign:'center'
    },
    head :{
        fontSize: 23,
        fontWeight: 'bold',
        textAlign:'center',
        marginTop:5,
        marginBottom:5
    },
    body: {
        fontSize: 15,
        marginBottom:5
    }
})

const questionInput = StyleSheet.create({
    container: {
        backgroundColor: COLORS.primaryBG,
        padding: 1,
        margin: 5,

        borderWidth: BORDER.borderWidth,
        borderColor: BORDER.borderColor,
        borderRadius: BORDER.borderRadius,
        
        flexDirection: "row",
        alignSelf:"center",
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
        alignSelf: 'center',
        backgroundColor: COLORS.secondaryBG,
        width:'auto',
        height:'auto'
    },
    empty: {
        alignSelf:'flex-end',
        justifyContent:'flex-end'
    }
})
export { main, questionInput, response, header, introduction}