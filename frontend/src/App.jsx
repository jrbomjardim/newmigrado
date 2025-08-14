import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
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
          {/* Adicione outras rotas aqui conforme o projeto avança */}
          <Route path="/" element={<LoginPage />} /> {/* Rota padrão para a página de login */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;


