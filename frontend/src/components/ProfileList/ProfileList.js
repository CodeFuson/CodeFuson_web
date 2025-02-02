// profilelist.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from './ProfileList.module.css';  // CSS Module importálása

const ProfileList = () => {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    // API hívás a Django backendhez
    axios.get('http://127.0.0.1:8000/api/v1/profiles/')  // Itt biztosan az api/v1/profiles/ végpontot használjuk
      .then(response => {
        setProfiles(response.data);
      })
      .catch(error => {
        console.error('Hiba történt a profilok betöltésekor:', error);
      });
  }, []);

  return (
    <div className={styles.profileList}>
      <h1>User Profile</h1>
      <ul>
        {profiles.length === 0 ? (
          <li>Nem található profil.</li>  // Ha nincs adat, jelenjen meg üzenet
        ) : (
          profiles.map(profile => (
            <li key={profile.id}>{profile.name}</li>
          ))
        )}
      </ul>
    </div>
  );
};

export default ProfileList;
