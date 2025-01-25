import React, { useState } from 'react';
import Editor from './Editor'; // Import the Editor component

function App() {
  const [script, setScript] = useState(''); // State to store the poem script

  // Function to update the poem script
  const handleScriptChange = (newScript) => {
    setScript(newScript); // Update the script state with the new poem text
  };

  return (
    <div className="App">
      <h1>Interactive Poem Platform</h1>
      <Editor onScriptChange={handleScriptChange} /> {/* Use the Editor component */}
      <h3>Current Poem Script</h3>
      <pre>{script}</pre> {/* Display the poem text as the user types */}
    </div>
  );
}

export default App;
