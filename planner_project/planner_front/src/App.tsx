import { Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./components/Header";
import EventPage from "./pages/EventPage";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<EventPage />} />
        <Route path="/events" element={<EventPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
      </Routes>
    </>
  );
}

export default App;
