import logo from './logo.svg';

import React, { useState, useEffect } from 'react';

import './App.css';

async function fetchData(){
  const response = await fetch('http://127.0.0.1:5000/materiaprimas')
  const data = await response.json();
  return data;
}



function App() {

  const [materiasPrimas, setMateriasPrimas] = useState([])

    useEffect(() => {
      async function getMateriasPrimas() {
        const data = await fetchData();
        setMateriasPrimas(data);
      }
      getMateriasPrimas();
    }, []);



  return (
    <div>
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Descrição</th>
          <th>Estoque</th>
        </tr>
      </thead>
      <tbody>
        {materiasPrimas.map(materiaPrima => (
          <tr key={materiaPrima.Id}>
            <td>{materiaPrima.Id}</td>
            <td>{materiaPrima.Descricao}</td>
            <td>{materiaPrima.Estoque}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  
  );
}

export default App;
