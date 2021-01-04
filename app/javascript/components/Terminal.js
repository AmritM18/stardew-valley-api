import React from "react"

import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { getItems } from '../redux/actions';

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
      for(let i = 0; i<command.length; i++) {
        command[i] = this.capitalize(command[i]);
      }

      // Check for special commands
      if(command.length === 1) {
        if(command[0] === "Help") {
          window.open("/help");
          e.target.value = "";
          return;
        }
        else if(command[0] === "Clear") {
          this.setState({ results: [] })
          e.target.value = "";
          return;
        }
        else if(command[0] === "Remove") {
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

      // Format command to be displayed on terminal
      let allWords = "";
      command.forEach((word) => {
        allWords += word + " ";
      })
      allWords = allWords.slice(0, -1);
      let terminal = this.state.results;
      terminal.push("$ " + allWords);

      let category = "";
      let field = "";
      if(this.props.map.has(allWords)) {
        category = this.props.map.get(allWords);
        command[0] = allWords;
      }
      else if(command.length > 1) {
        let removeLastWord = allWords.substring(0, allWords.lastIndexOf(" "));
        if(this.props.map.has(removeLastWord)) category = this.props.map.get(removeLastWord);
        command[0] = removeLastWord;
        field = command[command.length-1].toLowerCase();
      }

      if(category === "") {
        terminal.push("Invalid Command");
        this.setState({ results: terminal });
      }
      else {
        let url = "/" + category + "?q=" + command[0].replace(" ", "+");
        console.log(url)
        $.getJSON(url)
          .then(response => {
            const keys = Object.keys(response.data[0]);
            const values = Object.values(response.data[0]);

            if(field === "") {
              for(let i = 0; i<keys.length; i++) {
                if(keys[i] !== "name") {
                  //if(category === "season" && Array.isArray(values[i])) {
                  if(Array.isArray(values[i])) {
                    if(values[i].length !== 0) {
                      let string = this.capitalize(keys[i]) + ": "
                      for(let j = 0; j<values[i].length; j++) {
                        if(j === values[i].length-1) string += values[i][j].name;
                        else string += values[i][j].name + ", ";
                      }
                      terminal.push(string);
                    }
                  }
                  else if(values[i]) terminal.push(this.capitalize(keys[i]) + ": " + values[i]);
                  else terminal.push(this.capitalize(keys[i]) + ": None");
                }
              }
            }
            else {
              console.log(field);
              if(keys.includes(field) && field !== "name") {
                terminal.push(this.capitalize(field) + ": " + response.data[0][field]);
              }
              else {
                terminal.push("No Entries Found For " + command[0] + " " + this.capitalize(field));
              }
            }
            this.setState({ results: terminal })
          })
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
            <input type="text" className={"terminal-input terminal-input-"+(this.props.numTerminals < 3 ? 'large' : 'small')} onKeyDown={this._handleKeyDown} placeholder="Enter help to view commands" />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

const structuredSelector = createStructuredSelector({
  map: state => state.itemsReducer.map,
});

const mapDispatchToProps = { getItems };

// maps parts of the Redux State and Actions to this component's props
export default connect(structuredSelector, mapDispatchToProps)(Terminal);
//export default Terminal
