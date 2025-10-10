import React from 'react'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import ProtectedRoute from './components/ProtectedRoute'

//styles
import './styles/root.css'
import './styles/general.css'

function logout() {
  localStorage.clear; //TODO: Clear only the auth token
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear;
  return ( <Register />)
}

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<ProtectedRoute><Camera /></ProtectedRoute>} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<logout />} />
          <Route path="/register" element={<RegisterAndLogout />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
  )
}
export default App