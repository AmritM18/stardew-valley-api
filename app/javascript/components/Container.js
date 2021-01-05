import React from "react"
import Terminal from "./Terminal"

import { connect } from 'react-redux';
import { createStructuredSelector } from 'reselect';
import { getItems } from '../redux/actions';

class Container extends React.Component {
  constructor(props) {
    super(props);

    this.addTerminals = this.addTerminals.bind(this);
    this.removeTerminals = this.removeTerminals.bind(this);
  
    this.state = {
      numTerminals: 1
    };
  }

  handleGetItems = () => {
    this.props.getItems();
  };

  setFocus() {
    const inputs = document.getElementsByClassName("terminal-input");
    inputs[0].focus();
  }

  componentDidMount(){
    this.handleGetItems();
    this.setFocus();
  }

  addTerminals() {
    let maxTerms = 8;
    
    // Limiting number of terminals by screen size
    /*if(window.matchMedia("(max-width: 850px)").matches) {
      maxTerms = 1;
    }
    else if(window.matchMedia("(max-width: 1024px)").matches) {
      maxTerms = 4;
    }
    else if(window.matchMedia("(max-width: 1180px)").matches) {
      maxTerms = 6;
    }*/

    if(this.state.numTerminals < maxTerms) {
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
          content={this.props.terminals[i]}
          index={i}
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

const structuredSelector = createStructuredSelector({
    terminals: state => state.terminalsReducer.terminals
});

const mapDispatchToProps = { getItems };

// maps parts of the Redux State and Actions to this component's props
export default connect(structuredSelector, mapDispatchToProps)(Container);
//export default Container;