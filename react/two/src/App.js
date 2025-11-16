import { useState } from 'react';
import './App.css';
// import Counter from './Counter';
// import Person from './Person';
// import Modal from './Modal';
// import Item from './Item';
import Task from './Task';
import Form from './Form';


function App() {
  let [tasks, setTasks] = useState([{
    text: "Выучить JavaScript",
    done: false
  },
  {
    text: "Познакомиться с React",
    done: false
  },
  {
    text: "Устроиться на работу",
    done: false
  }
])

let addTask = text => {
  let newTask = [...tasks,{text}];
  setTasks(newTask);
}

let doneTask = index => {
  let newTask = [...tasks];
  newTask[index].done = true;
  setTasks(newTask);
}

  return (
    <div className="App">
    {/* <Counter />
    <Person /> */}
    {/* <Modal /> */}
    {/* <Item /> */}
    <div className='task-list'>
      {
        tasks.map((task, index) => (
          <Task 
          key={index}
          task={task}
          doneTask={doneTask}
          index={index}
          />
          
        ))
      }
      <Form addTask={addTask} />
    </div>
    </div>
  );
}

export default App;
