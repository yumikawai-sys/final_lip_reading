import './App.css';
import VideoRecorder from "./VideoRecorder";
import { useState } from 'react';


function App() {
  const [filePath, setFilePath] = useState('C:/Users/Yumi/Downloads/nsccassignment_test.mp4');
  const [predict, setPredict] = useState('');

  async function getPredict() {
    setFilePath('');

    try {
      const resp = await fetch('http://localhost:5000/predictions');
      const json = await resp.json();
      console.log(json);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  async function postPredict() {
    if (filePath === '') {
      return;
    }
    setPredict('');
    try {
      const resp = await fetch('http://localhost:5000/prediction/new', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filePath: filePath }),
      });
      const json = await resp.json();
      console.log(json);
      setPredict(json);
      setFilePath('');
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  return (
    <div className='main'>
      <VideoRecorder />
      <div className='buttons'>
        <button onClick={getPredict}>History</button>
        <button onClick={postPredict}>Transcript</button>
      </div>
      {predict&&
      <div>
        <h2 className='prediction'>Transcription: [ <span style={{color: 'rgb(1, 248, 165)'}}>{predict}</span> ]</h2>
      </div>}
    </div>
  );
}

export default App;
