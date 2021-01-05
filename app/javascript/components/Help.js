import React from "react"

class Help extends React.Component {
  render () {
    return (
      <React.Fragment>
        <div className="help-container">
          <div className="help-title">Stardew Valley API Help</div>
          <div className="help-subtitle">Contents</div>
          <ol>
            <li><a href="#general">General Commands</a></li>
            <li><a href="#villager">Villager Commands</a></li>
            <li><a href="#season">Season Commands</a></li>
          </ol>

          <div id="general" className="help-subtitle">General Commands</div>
          <table className="help-table">
            <tr>
              <td>Clear</td>
              <td>Does some stuff...</td>
            </tr>
            <tr>
              <td>Remove</td>
              <td>Does some stuff...</td>
            </tr>
            <tr>
              <td>New</td>
              <td>Does some stuff...</td>
            </tr>
            <tr>
              <td>Exit</td>
              <td>Does some stuff...</td>
            </tr>
          </table>

          <div id="villager" className="help-subtitle">Villager Commands</div>
          <div className="help-command">
            [Villager Name] [Birthday, Loves, Likes, Neutral, Dislikes, Hates (optional)]
          </div>

          <div id="season" className="help-subtitle">Season Commands</div>
        </div>
      </React.Fragment>
    );
  }
}

export default Help
