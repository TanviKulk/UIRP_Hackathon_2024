import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import './App.css'; // Import the CSS file for styling
import weedinatorLogo from './logo.png';

function App() {
  const [weedInfo, setWeedInfo] = useState(null);
  const [hasImage, setHasImage] = useState(false);

  const onDrop = (acceptedFiles) => {
    const file = acceptedFiles[0];
    setHasImage(true);

    const formData = new FormData();
    formData.append('file', file);
    formData.append('filename', file.name); 
    fetch('http://localhost:4000/analyze', {
      method: 'POST',
      body: formData
    })
      .then(response => response.json())
      .then(data => {
        setWeedInfo(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop, accept: 'image/*' });

  return (
    <div className="App">
      <header className="header">
        <img src={weedinatorLogo} alt="Weedinator Logo" className="logo" />
      </header>
      <main className={`main-content ${hasImage ? 'plain-bg' : ''}`}>
        <div {...getRootProps({ className: 'dropzone' })}>
          <input {...getInputProps()} />
          <p style={{ fontFamily: 'Times New Roman' }}>Drag 'n' drop a picture of a weed here, or click to select a file</p>
        </div>
        {weedInfo && (
          <div className="App-info" style={{ fontFamily: 'Times New Roman', alignContent: 'center' }}>
            <h2>Plant Information:</h2>
            <p>Is it a weed? {weedInfo.is_weed ? 'Yes' : 'No'}</p>
            <p>Weed Species: {weedInfo.weed_species}</p>
            <p>Eradication methods: {weedInfo.eradication_methods}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
