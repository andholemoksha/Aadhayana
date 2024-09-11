import React, { useState } from 'react';
import './Home.css'; // Import CSS file for styling
import { useNavigate } from 'react-router-dom';
const Home = () => {

    const navigate = useNavigate();

    const handleClick = () => {
      navigate('/upload'); // Navigate to the Upload page
    };
  
    return (
      <div className="login-container">
        <button onClick={handleClick} className="sign-in-button">
          Sign in
        </button>
      </div>
    );
//   const [phone, setPhone] = useState('');
//   const [message, setMessage] = useState('');

//   const handleGetOtp = () => {
//     if (phone.length !== 10) {
//       setMessage("Please enter a valid 10-digit phone number.");
//       return;
//     }
//     // Simulate OTP sending
//     setMessage(`OTP has been sent to ${phone}`);
//   };

//   return (
//     <div className="container">
//       <h2>Login with OTP</h2>
//       <div className="input-group">
//         <label htmlFor="phone">Enter your phone number:</label>
//         <input
//           type="number"
//           id="phone"
//           value={phone}
//           onChange={(e) => setPhone(e.target.value)}
//           placeholder="Enter phone number"
//           required
//         />
//       </div>
//       <input
//         type="submit"
//         id="getOtpBtn"
//         value="Get OTP"
//         onClick={handleGetOtp}
//       />
//       <div className="message">
//         {message}
//       </div>
//     </div>

};

export default Home;
