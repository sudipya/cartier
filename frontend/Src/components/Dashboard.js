import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  BarChart,
  Bar,
  Legend,
  ResponsiveContainer
} from "recharts";

const API = "http://localhost:8000";

function Dashboard() {

  const [attacks, setAttacks] = useState([]);
  const [stats, setStats] = useState({
    SQLi: 0,
    XSS: 0,
    SSRF: 0,
    RCE: 0
  });

  const fetchAnalytics = async () => {
    try {
      const res = await axios.get(`${API}/analytics`);
      const data = res.data;
      setAttacks(data);

      const counts = { SQLi: 0, XSS: 0, SSRF: 0, RCE: 0 };

      data.forEach((a) => {
        if (counts[a.attack_type] !== undefined) {
          counts[a.attack_type] += 1;
        }
      });

      setStats(counts);

    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const chartData = [
    { name: "SQL Injection", value: stats.SQLi },
    { name: "XSS", value: stats.XSS },
    { name: "SSRF", value: stats.SSRF },
    { name: "RCE", value: stats.RCE }
  ];

  return (
    <div style={{ padding: "30px" }}>

      <h1>Cartier WAF Dashboard</h1>

      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        <div className="card">SQLi Attacks: {stats.SQLi}</div>
        <div className="card">XSS Attacks: {stats.XSS}</div>
        <div className="card">SSRF Attacks: {stats.SSRF}</div>
        <div className="card">RCE Attacks: {stats.RCE}</div>
      </div>

      <h2 style={{ marginTop: "40px" }}>Attack Distribution</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" />
        </BarChart>
      </ResponsiveContainer>

      <h2 style={{ marginTop: "40px" }}>Recent Attacks</h2>

      <table border="1" width="100%" cellPadding="10">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Attack Type</th>
            <th>Payload</th>
            <th>Confidence</th>
          </tr>
        </thead>

        <tbody>
          {attacks.map((a, i) => (
            <tr key={i}>
              <td>{a.timestamp}</td>
              <td>{a.attack_type}</td>
              <td>{a.payload}</td>
              <td>{a.confidence}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default Dashboard;
