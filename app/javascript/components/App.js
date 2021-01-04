import React from "react"
import Container from "./Container"
import { Provider } from 'react-redux'
import configureStore from '../redux/store'

const store = configureStore();

class App extends React.Component {
  render () {
    return (
      <React.Fragment>
        <Provider store={store}>
          <Container></Container>
        </Provider>
      </React.Fragment>
    );
  }
}

export default App
