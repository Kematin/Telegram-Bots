import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import Logs from "./pages/Logs/Logs";
import AddProject from "./pages/AddProject/AddProject";
import Projects from "./pages/Projects/Projects";
import Undefined from "./pages/Undefined/Undefined";
import ProjectCatergory from "./pages/ProjectCategory/ProjectCatergory";
import Login from "./pages/Login/Login";
import "./App.css";

function App() {
  return (
    <div id="app">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Projects />} />
          <Route path="/add" element={<AddProject />} />
          <Route path="/logs" element={<Logs />} />
          <Route path="/login" element={<Login />} />
          <Route path="/:category" element={<ProjectCatergory />} />
          <Route path="*" element={<Undefined />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
