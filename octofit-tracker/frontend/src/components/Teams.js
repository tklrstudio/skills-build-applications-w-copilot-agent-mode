import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/teams/')
      .then(res => res.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h2>Teams</h2>
      <ul>{teams.map(t => <li key={t.id}>{t.name}</li>)}</ul>
    </div>
  );
}

export default Teams;
