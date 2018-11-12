import React from 'react';
const Todo = props =>
  <div className="pure-u-1-3">
    <h2>{props.title}</h2>
    <p>{props.description}</p>
  </div>;

export default Todo;