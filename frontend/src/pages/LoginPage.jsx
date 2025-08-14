import React, { useState } from 'react';
import { motion } from 'framer-motion';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login attempt:', { email, password });
    // TODO: Implement actual login logic with backend
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-600 p-4 relative overflow-hidden">
      {/* Floating animated elements */}
      <motion.div
        className="absolute bg-white bg-opacity-20 rounded-full filter blur-xl"
        initial={{ x: -200, y: -200, scale: 0.5, opacity: 0.3 }}
        animate={{ x: 200, y: 200, scale: 1.2, opacity: 0.5, rotate: 360 }}
        transition={{ duration: 15, repeat: Infinity, ease: "linear" }}
        style={{ width: '300px', height: '300px' }}
      />
      <motion.div
        className="absolute bg-white bg-opacity-20 rounded-full filter blur-xl"
        initial={{ x: 200, y: 200, scale: 0.7, opacity: 0.4 }}
        animate={{ x: -200, y: -200, scale: 1.0, opacity: 0.6, rotate: -360 }}
        transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
        style={{ width: '250px', height: '250px' }}
      />

      <motion.div
        className="relative bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg rounded-xl shadow-2xl p-8 w-full max-w-md border border-gray-200 border-opacity-30"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        <h2 className="text-3xl font-bold text-white text-center mb-6">Login</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-white text-sm font-bold mb-2" htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              className="w-full px-4 py-2 rounded-lg bg-white bg-opacity-20 border border-white border-opacity-30 text-white placeholder-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300"
              placeholder="seu@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-6 relative">
            <label className="block text-white text-sm font-bold mb-2" htmlFor="password">Senha</label>
            <input
              type={showPassword ? 'text' : 'password'}
              id="password"
              className="w-full px-4 py-2 rounded-lg bg-white bg-opacity-20 border border-white border-opacity-30 text-white placeholder-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-300 transition duration-300 pr-10"
              placeholder="********"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <button
              type="button"
              className="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5 text-white opacity-70 hover:opacity-100 transition duration-300"
              onClick={() => setShowPassword(!showPassword)}
              style={{ top: '60%' }} // Adjust position to align with input
            >
              {showPassword ? (
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M3.98 8.223A10.472 10.472 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.5-.241.807-.529 1.579-.88 2.307M9.5 12a2.5 2.5 0 1 1 5 0 2.5 2.5 0 0 1-5 0Z" />
                  <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 2.25 21.75 21.75" />
                </svg>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" />
                  <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                </svg>
              )}
            </button>
          </div>
          <motion.button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition duration-300 font-bold"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Entrar
          </motion.button>
        </form>
        <p className="text-center text-white text-sm mt-4">
          Não tem uma conta? <a href="#" className="font-bold hover:underline">Cadastre-se</a>
        </p>
      </motion.div>
    </div>
  );
};

export default LoginPage;


