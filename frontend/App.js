import React, { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const response = await fetch('http://localhost:8000/generate-infra', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, environment: 'dev' })
    });
    const data = await response.json();
    console.log("Generated Terraform:", data.code);
    setLoading(false);
    alert("Plan generated! Check GitHub Actions to approve.");
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Aetheria Platform Portal</h1>
      <p>Describe the infrastructure you need:</p>
      <textarea 
        style={{ width: '100%', height: '100px' }}
        placeholder='e.g., I need a private S3 bucket in us-east-1 with versioning enabled'
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Provision Resources"}
      </button>
    </div>
  );
}

export default App;