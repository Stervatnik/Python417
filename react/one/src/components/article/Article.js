import './Article.css';
import mars from './icons/mars.png'
import female from './icons/female.png'

function Article(props){
    let {db} = props;
    let icon;
    return(
        
        <article className='app'>
            {
                Object.keys(db).map((elem, index) =>{
                    if(db[elem].sex == 'female'){
                        icon = female;
                    } else {
                        icon = mars;
                    }
                    return(
                        <div className="card" key={index}>
                <img src={db[elem].photo} alt="" />
                <div className="name">
                    {db[elem].name} {db[elem].surname}
                </div>
                <div className="pol">
                    <img src={icon} alt="" />
                </div>
                <div className="age">
                    {db[elem].age}
                </div>
            </div>
                    )
                })
            }
            
        </article>
        
    )
}

export default Article