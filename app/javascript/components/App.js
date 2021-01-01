import React from "react"
import PropTypes from "prop-types"
import Terminal from "./Terminal"
class App extends React.Component {
  render () {
    return (
      <React.Fragment>
        <div className="container">
          <div className="flex-container">
            <Terminal></Terminal>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default App
