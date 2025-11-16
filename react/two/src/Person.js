import { useState } from "react";

function Person(){
    let[person, setPerson] = useState({
        firstName: 'Dmitriy',
        lastName: "Smirnov"
    })

    function rename(){
        // setPerson({firstName: "Sergey", lastName: person.lastName})
        setPerson({...person, firstName: "Sergey"})
    }

    return(
        <div>
            <p>{person.firstName} {person.lastName}</p>
            <button onClick={rename}>Rename</button>
        </div>
    )
}

export default Person