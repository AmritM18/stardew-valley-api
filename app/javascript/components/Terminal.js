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

      // Check for special commands
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

      // Format command to be displayed on terminal
      let input = "";
      command.forEach((word) => {
        input += this.capitalize(word) + " ";
      })
      let terminal = this.state.results;
      terminal.push("$ "+input);

      // Category is the type of item being searched for
      let category = "";
      // In case the name of the item is 2 or 3 words long
      let twoWords = "";
      let threeWords = "";
      if(command.length > 1) twoWords = this.capitalize(command[0]) + " " + this.capitalize(command[1]);
      if(command.length > 2) threeWords = this.capitalize(command[0]) + " " + this.capitalize(command[1]) + " " + this.capitalize(command[2]);

      switch(true) {
        case this.props.villagers.includes(command[0].toLowerCase()):
          category = "villager";
          command[0] = this.capitalize(command[0]);
          break;
        case this.props.seasons.includes(command[0].toLowerCase()):
          category = "season";
          command[0] = this.capitalize(command[0]);
          break;
        case this.props.crops.includes(threeWords.toLowerCase()):
          category = "crop";
          command[0] = threeWords.replace(" ", "+");
          command.splice(2, 1);
          command.splice(1, 1);
          break;
        case this.props.crops.includes(twoWords.toLowerCase()):
          category = "crop";
          command[0] = twoWords.replace(" ", "+");
          command.splice(1, 1);
          break;
        case this.props.crops.includes(command[0].toLowerCase()):
          category = "crop";
          command[0] = this.capitalize(command[0]);
          break;
      }

      if(category === "" || command.length > 2) {
        terminal.push("Invalid Command");
        this.setState({ results: terminal });
      }
      else {
        let url = "/" + category + "?q=" + command[0];
        console.log(url)
        $.getJSON(url)
          .then(response => {
            const keys = Object.keys(response.data[0]);
            const values = Object.values(response.data[0]);

            if(command.length === 1) {
              for(let i = 0; i<keys.length; i++) {
                if(keys[i] !== "name") {
                  if(category === "season" && Array.isArray(values[i])) {
                    if(values[i].length !== 0) {
                      let string = this.capitalize(keys[i]) + ": "
                      for(let j = 0; j<values[i].length; j++) {
                        // TO DO: CHANGE .CROP TO .NAME ONCE MODELS ARE CHANGED
                        if(j === values[i].length-1) string += values[i][j].crop;
                        else string += values[i][j].crop + ", ";
                      }
                      terminal.push(string);
                    }
                  }
                  else if(values[i]) terminal.push(this.capitalize(keys[i]) + ": " + values[i]);
                  else terminal.push(this.capitalize(keys[i]) + ": None");
                }
              }
            }
            else if(command.length === 2) {
              const field = command[1].toLowerCase();
              if(keys.includes(field) && field !== "name") {
                terminal.push(this.capitalize(field) + ": " + response.data[0][field]);
              }
              else {
                terminal.push("No Entries Found For " + this.capitalize(command[0]) + " " + this.capitalize(field));
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

export default Terminal
