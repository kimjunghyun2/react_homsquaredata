import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';

import Home from './pages/home';
import Search from './pages/search';
import Register from './pages/register';
import SendMail from './pages/sendmail';
import SearchResult from './pages/searchresult';

function App() {
  return (
   <BrowserRouter>
      <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/search' element={<Search/>}/>
          <Route path='/register' element={<Register/>}/>
          <Route path='/sendmail' element={<SendMail/>}/>
          <Route path='/searchresult' element={<SearchResult/>}/>
      </Routes>
   </BrowserRouter>
  );
}

export default App;
