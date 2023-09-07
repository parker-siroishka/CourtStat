import React, { useState, useEffect } from 'react';
import axios from 'axios';

function List() {
  const [teams, setTeams] = useState();
  const [loading, setLoading] = useState(true);

  const getData = async () => {
    try {
      const { data } = await axios.get(`http://localhost:8000/player/`);
      setTeams(data.data[0]);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  if (loading) {
    return; // Render a loading indicator
  }

  return (
    <div>
      {loading && <p>Loading...</p>}
      {teams.map((player, index) => (
        <div key={index}>
          <p>Player: {player.Name}</p>
          <p>Team: {player.Team}</p>
          <br />
        </div>
      ))}
    </div>
  );
}

export default List;
