import React, { useState, useEffect } from 'react';

const TestTimer = ({ initialTimeInSeconds }) => {
  const [remainingTime, setRemainingTime] = useState(initialTimeInSeconds);

  useEffect(() => {
    if (remainingTime <= 0) return;

    const timer = setInterval(() => {
      setRemainingTime((prevTime) => prevTime - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [remainingTime]);

  const formatTime = (totalSeconds) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };

  if (remainingTime <= 0) {
    return <p className="text-red-500 font-bold">Tempo de teste esgotado!</p>;
  }

  return (
    <div className="text-white text-sm font-semibold bg-gray-800 bg-opacity-50 rounded-md px-3 py-1">
      Tempo restante: {formatTime(remainingTime)}
    </div>
  );
};

export default TestTimer;


