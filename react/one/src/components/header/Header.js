import './Header.css';
import logo from './logo.svg';

function Header(props){
    let{text, slogan} = props
    return(
        <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>{text}</h1>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        {slogan}
      </header>
    )
}

export default Header