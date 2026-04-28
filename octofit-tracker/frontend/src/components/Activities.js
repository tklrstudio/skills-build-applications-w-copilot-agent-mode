import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/activities/')
      .then(res => res.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h2>Activities</h2>
      <ul>{activities.map(a => <li key={a.id}>{a.name}</li>)}</ul>
    </div>
  );
}

export default Activities;
