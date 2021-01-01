import React from "react"
import PropTypes from "prop-types"
class Terminal extends React.Component {
  render () {
    return (
      <React.Fragment>
        <div className="terminal-container">
          <div className="terminal-header">
            Stardew Valley API
          </div>
          <div className="terminal-body">
            <input type="text" className="terminal-input"></input>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Terminal
