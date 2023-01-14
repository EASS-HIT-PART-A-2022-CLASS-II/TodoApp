import React, { useState, useEffect } from 'react';
import TodoView from './components/TodoListView';
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')
  const [id, setId] = useState('')


  // Read all todos
  useEffect(() => {
    axios.get('http://localhost:8080/todo/')
      .then(res => {
        setTodoList(res.data)
      })
  });

  // Post a todo
  const addTodoHandler = () => {
    axios.post('http://localhost:8080/todo/', { "title": title, "description": desc })
      .then(res => console.log(res))
  };

  // Edit a todo
  const editTodoHandler = () => {
    axios.get(`http://localhost:8080/todo/id/${title}`)
      .then(res => { setId(res.data) })
    axios.put(`http://localhost:8080/todo/${id}`, { "title": title, "description": desc })
      .then(res => console.log(res))
  }

  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{ "width": "400px", "backgroundColor": "white", "marginTop": "20px" }} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">ToDo List</h1>
      <h6 className="card text-white bg-primary mb-1">EASS Project 2022</h6>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" onChange={event => setTitle(event.target.value)} placeholder='Title' />
          <input className="mb-2 form-control desIn" onChange={event => setDesc(event.target.value)} placeholder='Description' />
          <button className="btn btn-outline-primary mx-2 mb-3" style={{ 'borderRadius': '50px', "font-weight": "bold" }} onClick={addTodoHandler}>Add</button>
          <button className="btn btn-outline-primary mx-2 mb-3" style={{ 'borderRadius': '50px', "font-weight": "bold" }} onClick={editTodoHandler}>Edit</button>
        </span>
        <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
        <div >
          <TodoView todoList={todoList} />
        </div>
      </div>
    </div>
  );
}

export default App;