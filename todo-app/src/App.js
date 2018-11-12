import React, { Component } from 'react';
import './App.css';
import data from './data';
import Todo from './Todo';

class App extends Component {
  componentWillMount() {
    this.setState({
      todos: data,
    });
  }

  addTodo = (e) => {
    e.preventDefault();

    const todos = this.state.todos;
    const newId = todos[todos.length - 1].id + 1;

    this.setState({
      todos: todos.concat({ id: newId,
                            title: `New Todo ${newId}`,
                            description: `${newId} description`}),
    });
  }
  newTodo = () =>
    <div className="pure-g">
      <div className='pure-u-12-24'>
        <form className="pure-form">
          <fieldset>
            <legend>New todo</legend>

            <input placeholder="Title" />
            <input placeholder="Description" />

            <button type="submit" className="pure-button pure-button-primary" >Add</button>
          </fieldset>
        </form>
      </div>
    </div>;

  render() {
    return (
      <div className="App">
        {this.newTodo()}
        <div className="pure-g">
          {this.state.todos.map(info =>
            <Todo key = {info.id} {...info}/>
            )}
        </div>
      </div>
    );
  }
}

export default App;
