import React from 'react';
import {
    Plattform,
    Stylesheet,
    View,
    Text
} from 'react-native'

const instruction = Plattform.select({
    ios: 'Press Cmd+R to reload,\n',
    android: 'Double tap R on your keyboard to reload'
});

type Props = {};
export default class App extends Component <Props> {
    render(){
        return (
            <View>

            </View>
        )
    }
}

const styles = Stylesheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#ffffff'
    },
    welcome: {
        fontSize: 20,
        textAlign: 'center',
        margin: 10,
    },
    instruction: {
        textAlign: 'center',
        colour: '#333333',
        marginBottom: '5',
    },

});


import React from 'react'
import { TouchableOpacity, Text } from 'react-native'
import { Actions } from 'react-native-router-flux'

const About = () => {
   const goToHome = () => {
      Actions.home()
   }
   return (
      <TouchableOpacity style = {{ margin: 128 }} onPress = {goToHome}>
         <Text>This is ABOUT</Text>
      </TouchableOpacity>
   )
}
export default About

import React, { Component } from 'react'
import { View, Switch, StyleSheet }

from 'react-native'

export default SwitchExample = (props) => {
   return (
      <View style = {styles.container}>
         <Switch
         onValueChange = {props.toggleSwitch1}
         value = {props.switch1Value}/>
      </View>
   )
}
const styles = StyleSheet.create ({
   container: {
      flex: 1,
      alignItems: 'center',
      marginTop: 100
   }
})

import React, { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'

class Inputs extends Component {
   state = {
      email: '',
      password: ''
   }
   handleEmail = (text) => {
      this.setState({ email: text })
   }
   handlePassword = (text) => {
      this.setState({ password: text })
   }
   login = (email, pass) => {
      alert('email: ' + email + ' password: ' + pass)
   }
   render() {
      return (
         <View style = {styles.container}>
            <TextInput style = {styles.input}
               underlineColorAndroid = "transparent"
               placeholder = "Email"
               placeholderTextColor = "#9a73ef"
               autoCapitalize = "none"
               onChangeText = {this.handleEmail}/>
            
            <TextInput style = {styles.input}
               underlineColorAndroid = "transparent"
               placeholder = "Password"
               placeholderTextColor = "#9a73ef"
               autoCapitalize = "none"
               onChangeText = {this.handlePassword}/>
            
            <TouchableOpacity
               style = {styles.submitButton}
               onPress = {
                  () => this.login(this.state.email, this.state.password)
               }>
               <Text style = {styles.submitButtonText}> Submit </Text>
            </TouchableOpacity>
         </View>
      )
   }
}
export default Inputs

const styles = StyleSheet.create({
   container: {
      paddingTop: 23
   },
   input: {
      margin: 15,
      height: 40,
      borderColor: '#7a42f4',
      borderWidth: 1
   },
   submitButton: {
      backgroundColor: '#7a42f4',
      padding: 10,
      margin: 15,
      height: 40,
   },
   submitButtonText:{
      color: 'white'
   }
})



import React, { Component } from 'react';
import { Text, Image, View, StyleSheet, ScrollView } from 'react-native';

class ScrollViewExample extends Component {
   state = {
      names: [
         {'name': 'Ben', 'id': 1},
         {'name': 'Susan', 'id': 2},
         {'name': 'Robert', 'id': 3},
         {'name': 'Mary', 'id': 4},
         {'name': 'Daniel', 'id': 5},
         {'name': 'Laura', 'id': 6},
         {'name': 'John', 'id': 7},
         {'name': 'Debra', 'id': 8},
         {'name': 'Aron', 'id': 9},
         {'name': 'Ann', 'id': 10},
         {'name': 'Steve', 'id': 11},
         {'name': 'Olivia', 'id': 12}
      ]
   }
   render() {
      return (
         <View>
            <ScrollView>
               {
                  this.state.names.map((item, index) => (
                     <View key = {item.id} style = {styles.item}>
                        <Text>{item.name}</Text>
                     </View>
                  ))
               }
            </ScrollView>
         </View>
      )
   }
}
export default ScrollViewExample

const styles = StyleSheet.create ({
   item: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: 30,
      margin: 2,
      borderColor: '#2a4944',
      borderWidth: 1,
      backgroundColor: '#d2f7f1'
   }
})


import React from "react";
import { ImageBackground, StyleSheet, Text, View } from "react-native";

const image = { uri: "https://reactjs.org/logo-og.png" };

export default App = () => (
  <View style={styles.container}>
    <ImageBackground source={image} style={styles.image}>
      <Text style={styles.text}>Inside</Text>
    </ImageBackground>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column"
  },
  image: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center"
  },
  text: {
    color: "grey",
    fontSize: 30,
    fontWeight: "bold"
  }
});

import React, { useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default App = () => {
  const [count, setCount] = useState(0);
  const onPress = () => setCount(prevCount => prevCount + 1);

  return (
    <View style={styles.container}>
      <View style={styles.countContainer}>
        <Text>Count: {count}</Text>
      </View>
      <TouchableOpacity
        style={styles.button}
        onPress={onPress}
      >
        <Text>Press Here</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    paddingHorizontal: 10
  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10
  },
  countContainer: {
    alignItems: "center",
    padding: 10
  }
});

import React, { useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default App = () => {
  const [count, setCount] = useState(0);
  const onPress = () => setCount(prevCount => prevCount + 1);

  return (
    <View style={styles.container}>
      <View style={styles.countContainer}>
        <Text>Count: {count}</Text>
      </View>
      <TouchableOpacity
        style={styles.button}
        onPress={onPress}
      >
        <Text>Press Here</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    paddingHorizontal: 10
  },
  button: {
    alignItems: "center",
    backgroundColor: "#DDDDDD",
    padding: 10
  },
  countContainer: {
    alignItems: "center",
    padding: 10
  }
});

/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from "react";
import { Platform, StyleSheet, Text, View, Alert, YellowBox} from "react-native";
import { Menu, MenuProvider, MenuOptions, MenuOption, MenuTrigger} from "react-native-popup-menu";

export default class HomeActivity extends Component {

  constructor(props) {
     super(props);
     YellowBox.ignoreWarnings([
      'Warning: isMounted(...) is deprecated', 'Module RCTImageLoader'
    ]);
   }

  render() {
    return (
      <MenuProvider style={{ flexDirection: "column", padding: 30 }}>
        <Menu onSelect={value => alert(`You Clicked : ${value}`)}>

          <MenuTrigger  >
          <Text style={styles.headerText}>DropDown Menu</Text>
          </MenuTrigger  >

          <MenuOptions>
            <MenuOption value={"Login"}>
              <Text style={styles.menuContent}>Login</Text>
            </MenuOption>
            <MenuOption value={"Register"}>
              <Text style={styles.menuContent}>Register</Text>
            </MenuOption>
            <MenuOption value={"Download"}>
              <Text style={styles.menuContent}>Download</Text>
            </MenuOption>
            <MenuOption value={"Logout"}>
              <Text style={styles.menuContent}>Logout</Text>
            </MenuOption>
            <MenuOption value={3} disabled={true}>
              <Text style={styles.menuContent}>Disabled Menu</Text>
            </MenuOption>
          </MenuOptions>

        </Menu>
      </MenuProvider>
    );
  }
}

const styles = StyleSheet.create({
    headerText: {
    fontSize: 20,
    margin: 10,
    fontWeight: "bold"
  },
  menuContent: {
    color: "#000",
    fontWeight: "bold",
    padding: 2,
    fontSize: 20
  }
});


// http://codesolution.co.in/detail/post/create-navigation-drawer--side-menu---in-react-native-using-react-navigation-v3
