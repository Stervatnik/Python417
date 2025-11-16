import './App.css';
import Article from '../article/Article';
import Header from '../header/Header';
import Footer from '../footer/Footer';
import Nav from '../nav/Nav';
import data from './db.json'

function App() {
  let title = "My Site"
  let slogan = "I am learning React"
  let nav = {"Главная": "/index", "Новости": "/news", "О компании": "/about", "Магазин": "/shop", "Контакты": "/contacts"}

  let db = data.people
  let copy = "Copyright - 2025"

  return (
    <div className="App">
      <Header text={title} slogan={slogan} />
      <Nav navigation={nav} />
      <Article db={db}/>
      <Footer copy={copy} />
      
        
    </div>
  );
}

export default App;
