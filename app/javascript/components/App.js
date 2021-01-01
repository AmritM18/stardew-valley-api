import React from "react"
import PropTypes from "prop-types"
import Terminal from "./Terminal"
class App extends React.Component {
  constructor(props) {
    super(props);

    this.addTerminals = this.addTerminals.bind(this);
    this.removeTerminals = this.removeTerminals.bind(this);
  
    this.state = {
      numTerminals: 1,
      villagers: []
    };
  }

  setFocus() {
    const inputs = document.getElementsByClassName("terminal-input");
    inputs[0].focus();
  }

  componentDidMount(){
    this.setFocus();

    $.getJSON('/villager')
        .then(response => {
          let villagerNames = [];
          for(let i = 0; i<response.data.length; i++) {
            villagerNames.push(response.data[i].name.toLowerCase())
          }
          this.setState({ villagers: villagerNames })
        })
  }

  addTerminals() {
    if(this.state.numTerminals !== 8) {
      this.setState({
        numTerminals: this.state.numTerminals + 1
      })
    }
    this.setFocus();
  }

  removeTerminals() {
    if(this.state.numTerminals !== 1) {
      this.setState({
        numTerminals: this.state.numTerminals - 1
      })
    }
    this.setFocus();
  }

  renderTerminals() {
    let terminals = [];
    const numTerms = this.state.numTerminals;
    for(let i = 0; i<numTerms; i++) {
      let marginBottom = numTerms > 2 && i < Math.ceil(numTerms / 2);
      terminals.push(
        <Terminal 
          key={i} 
          numTerminals={numTerms} 
          addTerms={this.addTerminals} 
          removeTerms={this.removeTerminals} 
          marginBottom={marginBottom}
          villagers={this.state.villagers}
        >
        </Terminal>
      );
    }
    return(<div className={"container-flex container-flex-"+numTerms}>{terminals}</div>);
  }

  render () {
    return (
      <React.Fragment>
        { this.renderTerminals() }
      </React.Fragment>
    );
  }
}

export default App
