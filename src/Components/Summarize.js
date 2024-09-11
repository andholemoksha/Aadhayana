import React, { useState } from 'react';
import axios from 'axios';
import { upload } from '@testing-library/user-event/dist/upload';

function Summarize() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert('Please select a file!');
      return;
    }

    const formData = new FormData()
    formData.append('file', file);

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setSummary(response.data.summary);
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Upload a PDF to Summarize</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept="application/pdf" />
        <button type="submit">Upload PDF</button>
      </form>

      {loading ? (
        <p>Loading...</p>
      ) : (
        summary && (
          <div>
            <h2>Summary:</h2>
            <p>{summary}</p>
          </div>
        )
      )}
    </div>
  );
}

export default Summarize;
