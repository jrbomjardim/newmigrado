import React from 'react';
import { motion } from 'framer-motion';

const HomePage = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600 p-4 relative overflow-hidden">
      {/* Floating animated elements */}
      <motion.div
        className="absolute bg-white bg-opacity-20 rounded-full filter blur-xl"
        initial={{ x: -300, y: -300, scale: 0.6, opacity: 0.3 }}
        animate={{ x: 300, y: 300, scale: 1.3, opacity: 0.5, rotate: 360 }}
        transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
        style={{ width: '400px', height: '400px' }}
      />
      <motion.div
        className="absolute bg-white bg-opacity-20 rounded-full filter blur-xl"
        initial={{ x: 300, y: 300, scale: 0.8, opacity: 0.4 }}
        animate={{ x: -300, y: -300, scale: 1.1, opacity: 0.6, rotate: -360 }}
        transition={{ duration: 25, repeat: Infinity, ease: "linear" }}
        style={{ width: '350px', height: '350px' }}
      />

      <motion.div
        className="relative bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-4xl border border-gray-200 border-opacity-30 text-white text-center"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        <h1 className="text-4xl font-bold mb-4">Bem-vindo ao Migrado!</h1>
        <p className="text-lg mb-8">Seu sistema completo de estudos por flashcards.</p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Exemplo de Card com efeito de vidro fosco */}
          <motion.div
            className="bg-white bg-opacity-15 backdrop-filter backdrop-blur-md rounded-lg p-6 shadow-lg border border-gray-200 border-opacity-30"
            whileHover={{ scale: 1.05, boxShadow: "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)" }}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2, ease: "easeOut" }}
          >
            <h3 className="text-xl font-semibold mb-2">Estude Eficientemente</h3>
            <p className="text-sm">Aproveite nossos flashcards para otimizar seu aprendizado e memorização.</p>
          </motion.div>

          <motion.div
            className="bg-white bg-opacity-15 backdrop-filter backdrop-blur-md rounded-lg p-6 shadow-lg border border-gray-200 border-opacity-30"
            whileHover={{ scale: 1.05, boxShadow: "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)" }}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4, ease: "easeOut" }}
          >
            <h3 className="text-xl font-semibold mb-2">Comunidade Ativa</h3>
            <p className="text-sm">Conecte-se com outros estudantes e compartilhe conhecimento.</p>
          </motion.div>

          <motion.div
            className="bg-white bg-opacity-15 backdrop-filter backdrop-blur-md rounded-lg p-6 shadow-lg border border-gray-200 border-opacity-30"
            whileHover={{ scale: 1.05, boxShadow: "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)" }}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.6, ease: "easeOut" }}
          >
            <h3 className="text-xl font-semibold mb-2">Acompanhe seu Progresso</h3>
            <p className="text-sm">Gráficos e estatísticas detalhadas para você monitorar sua evolução.</p>
          </motion.div>
        </div>
      </motion.div>
    </div>
  );
};

export default HomePage;


