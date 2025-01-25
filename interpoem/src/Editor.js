import React, { useState } from 'react';

const Editor = ({ onScriptChange }) => {
  const [script, setScript] = useState('');

  const handleChange = (e) => {
    const value = e.target.value;
    setScript(value); // Update the state with the new script
    onScriptChange(value); // Pass the script back to the parent component
  };

  return (
    <div>
      <h2>Interactive Poem Editor</h2>
      <textarea
        value={script}
        onChange={handleChange}
        rows={10}
        cols={50}
        placeholder="Write your interactive poem here..."
      />
    </div>
  );
};

export default Editor;
