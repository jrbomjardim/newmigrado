import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage'; // Importe o componente HomePage
import TestTimer from './components/TestTimer'; // Importe o componente TestTimer

function App() {
  // Simulação do tempo de teste restante (em segundos) para demonstração
  // Em uma implementação real, este valor viria do backend após o login
  const simulatedRemainingTime = 24 * 60 * 60; // 24 horas em segundos

  return (
    <Router>
      <div className="relative min-h-screen">
        {/* Contador de tempo de teste no topo */}
        <div className="absolute top-4 right-4 z-10">
          <TestTimer initialTimeInSeconds={simulatedRemainingTime} />
        </div>

        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/home" element={<HomePage />} /> {/* Nova rota para a página inicial */}
          <Route path="/" element={<HomePage />} /> {/* Rota padrão para a página inicial */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;


