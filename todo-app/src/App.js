import React, { Component } from 'react';
import './App.css';

const data = [
  {
    title: "build an API",
    description: "this is desc1",
  },
  {
    title: "write article",
    description: "this is desc1",
  },
  {
    title: "profit!",
    description: "this is desc1",
  },
]

const Todo = props =>
  <div className="pure-u-1-3">
    <h2>{props.title}</h2>
    <p>{props.description}</p>
  </div>;
class App extends Component {
  render() {
    return (
      <div className="App pure-g">
        {data.map(info =>
          <Todo {...info} />
          )}
      </div>
    );
  }
}

export default App;
