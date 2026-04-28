import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch('https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setEntries(data));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>{entries.map(e => <li key={e.id}>{e.username}: {e.score}</li>)}</ul>
    </div>
  );
}

export default Leaderboard;
