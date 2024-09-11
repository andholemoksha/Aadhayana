// import Upload from './Components/Upload';
import logo from './logo.svg';
import Home from './Components/Home';
import Summarize from './Components/Summarize';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Summarize />} />
      </Routes>
    </Router>      </header>
    </div>
  );
}

export default App;
