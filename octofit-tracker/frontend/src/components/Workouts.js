import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/workouts/')
      .then(res => res.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>{workouts.map(w => <li key={w.id}>{w.name}</li>)}</ul>
    </div>
  );
}

export default Workouts;
