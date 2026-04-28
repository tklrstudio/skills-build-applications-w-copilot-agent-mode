import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://jasontklr-skills-build-applications-w-copilot-agent-mode-8000.app.github.dev/api/users/')
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h2>Users</h2>
      <ul>{users.map(u => <li key={u.id}>{u.username}</li>)}</ul>
    </div>
  );
}

export default Users;
