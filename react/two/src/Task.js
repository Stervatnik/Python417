

function Task(props){
    let {task, doneTask, index} = props
    return(
        <div className="task" style={{textDecoration: task.done ? 'line-through' : ''}}>
            {task.text}
            <div>
                <button onClick={() => doneTask(index)}>Done</button>
            </div>
        </div>
    )
}

export default Task