import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {

  const [requestInput, setRequestInput] = useState("");
  const [result, setResult] = useState(null);
  const [attacks, setAttacks] = useState([]);

  const API = "http://localhost:8000";

  const detectAttack = async () => {
    try {
      const response = await axios.post(`${API}/detect`, {
        payload: requestInput
      });

      setResult(response.data);
      loadAnalytics();

    } catch (error) {
      console.error("Detection error:", error);
    }
  };

  const loadAnalytics = async () => {
    try {
      const response = await axios.get(`${API}/analytics`);
      setAttacks(response.data);
    } catch (error) {
      console.error("Analytics error:", error);
    }
  };

  useEffect(() => {
    loadAnalytics();
  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Cartier WAF Dashboard</h1>
      <p>AI-Powered Web Attack Detection System</p>

      <div style={{ marginTop: "30px" }}>
        <h2>Test Web Request</h2>

        <textarea
          rows="5"
          cols="80"
          placeholder="Paste HTTP request, URL, or payload..."
          value={requestInput}
          onChange={(e) => setRequestInput(e.target.value)}
        />

        <br /><br />

        <button onClick={detectAttack}>
          Detect Attack
        </button>
      </div>

      {result && (
        <div style={{ marginTop: "40px", border: "1px solid #ddd", padding: "20px" }}>
          <h2>Detection Result</h2>

          <p><b>Attack Detected:</b> {result.attack}</p>
          <p><b>Type:</b> {result.attack_type}</p>
          <p><b>Confidence:</b> {result.confidence}</p>

          <h3>Explainable Evidence</h3>
          <pre>{JSON.stringify(result.explanation, null, 2)}</pre>
        </div>
      )}

      <div style={{ marginTop: "50px" }}>
        <h2>Attack Analytics</h2>

        <table border="1" cellPadding="10">
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Attack Type</th>
              <th>Payload</th>
              <th>Confidence</th>
            </tr>
          </thead>

          <tbody>
            {attacks.map((attack, index) => (
              <tr key={index}>
                <td>{attack.timestamp}</td>
                <td>{attack.attack_type}</td>
                <td>{attack.payload}</td>
                <td>{attack.confidence}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}

export default App;
