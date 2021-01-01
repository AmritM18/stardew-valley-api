import React from "react"
import PropTypes from "prop-types"

class Terminal extends React.Component {
  constructor(props) {
    super(props);
  
    this.state = {
      results: []
    };
  }

  capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
  }

  _handleKeyDown = (e) => {
    if (e.key === 'Enter' && e.target.value !== "") {
      let command = e.target.value.split(" ");
      
      // Remove extra space at beginning and end
      if(command[0] === "") command.splice(0, 1);
      if(command[command.length-1] === "") command.splice(command.length-1, 1);

      if(command.length === 1) {
        if(command[0].toLowerCase() === "help") {
          window.open("/help");
          e.target.value = "";
          return;
        }
        else if(command[0].toLowerCase() === "clear") {
          this.setState({ results: [] })
          e.target.value = "";
          return;
        }
        else if(command[0].toLowerCase() === "remove") {
          let newResults = this.state.results;
          let popped = newResults.pop();
          while(popped.charAt(0) !== '$') {
            popped = newResults.pop();
          }
          this.setState({ results: newResults })
          e.target.value = "";
          return;
        }
      }

      let input = "";
      command.forEach((word) => {
        input += this.capitalize(word) + " ";
      })
      let terminal = this.state.results;
      terminal.push("$ "+input);

      if(command.length === 1 || command.length === 2) {
        if(this.props.villagers.includes(command[0].toLowerCase())) {
          $.getJSON('/villager?q=' + this.capitalize(command[0]))
            .then(response => {
              const keys = Object.keys(response.data[0]);
              const values = Object.values(response.data[0]);
              if(command.length === 1) {
                for(let i = 0; i<keys.length; i++) {
                  if(keys[i] !== "name") {
                    terminal.push(this.capitalize(keys[i]) + ": " + values[i]);
                  }
                }
              }
              else if(command.length === 2) {
                const field = command[1].toLowerCase();
                if(keys.includes(field)) {
                  terminal.push(this.capitalize(field) + ": " + response.data[0][field]);
                }
                else {
                  terminal.push("No Entries Found For " + this.capitalize(field));
                }
              }
              this.setState({ results: terminal })
            })
        }
        else {
          terminal.push("Invalid Command");
          this.setState({ results: terminal })
        }
      }
      else {
        terminal.push("Invalid Command");
        this.setState({ results: terminal })
      }

      // Clear the input field
      e.target.value = "";
    }
  }

  getResults() {
    let info = [];
    for(let i = 0; i<this.state.results.length; i++) {
      if(this.state.results[i].charAt(0) === '$' && i !== 0) {
        info.push(<div key={i} className="entry-start">{this.state.results[i]}</div>);
      }
      else {
        info.push(<div key={i}>{this.state.results[i]}</div>);
      }
    }
    return(<div>{info}</div>)
  }

  render () {
    return (
      <React.Fragment>
        <div className="terminal-container">
          <div className={"terminal-header terminal-header-" + this.props.numTerminals}>
            <div className={"terminal-button-" + (this.props.numTerminals < 3 ? 'large' : 'small')} onClick={this.props.removeTerms}>-</div>
            <div>Stardew Valley API</div>
            <div className={"terminal-button-" + (this.props.numTerminals < 3 ? 'large' : 'small')}  onClick={this.props.addTerms}>+</div>
          </div>
          <div className={"terminal-body terminal-body-" + this.props.numTerminals}>
            { this.getResults() }
          </div>
          <div className={ 'terminal-input-container' + (this.props.marginBottom ? ' terminal-margin-bottom' : '') }>
            <input type="text" className={"terminal-input terminal-input-"+(this.props.numTerminals < 3 ? 'large' : 'small')} onKeyDown={this._handleKeyDown} placeholder="Enter help to view available commands" />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Terminal
