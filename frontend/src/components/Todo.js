import axios from 'axios'
import React, { useState } from 'react';


function TodoItem(props) {

  const [id, setId] = useState('')
 
  // Delete a todo
  const deleteTodoHandler = (title) => {
    axios.get(`http://localhost:8080/todo/id/${title}`)
      .then(res => { setId(res.data) })
    axios.delete(`http://localhost:8080/todo/${id}`)
      .then(res => console.log(res.data))
  }

  return (
    <div>
      <p>
        <span style={{ fontWeight: 'bold, underline' }}>{props.todo.title} : </span> {props.todo.description}
        <button onClick={() => deleteTodoHandler(props.todo.title)} className="btn btn-outline-danger my-2 mx-2" style={{ 'borderRadius': '50px', }}>X</button>
        <hr></hr>
      </p>
    </div>
  )
}

export default TodoItem;