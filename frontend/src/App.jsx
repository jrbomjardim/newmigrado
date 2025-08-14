import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        {/* Adicione outras rotas aqui conforme o projeto avança */}
        <Route path="/" element={<LoginPage />} /> {/* Rota padrão para a página de login */}
      </Routes>
    </Router>
  );
}

export default App;


