import React from "react";

function AttackTable({ attacks }) {

  return (
    <div style={{ marginTop: "40px" }}>
      <h2>Detected Attacks</h2>

      <table border="1" width="100%" cellPadding="10" cellSpacing="0">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Attack Type</th>
            <th>Payload</th>
            <th>Confidence</th>
            <th>Explanation</th>
          </tr>
        </thead>

        <tbody>
          {attacks && attacks.length > 0 ? (
            attacks.map((attack, index) => (
              <tr key={index}>
                <td>{attack.timestamp}</td>
                <td>{attack.attack_type}</td>
                <td style={{ maxWidth: "400px", wordBreak: "break-all" }}>
                  {attack.payload}
                </td>
                <td>{attack.confidence}</td>
                <td>
                  {attack.explanation
                    ? JSON.stringify(attack.explanation)
                    : "N/A"}
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5" align="center">
                No attacks detected yet
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default AttackTable;
