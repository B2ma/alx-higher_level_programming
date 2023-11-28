#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Check if the movie data is valid
    if (response.statusCode === 200) {
      // Fetch character details for each character URL
      const fetchCharacterDetails = (characterUrl) => {
        return new Promise((resolve, reject) => {
          request(characterUrl, (characterError, characterResponse, characterBody) => {
            if (characterError) {
              reject(characterError);
            } else {
              const characterData = JSON.parse(characterBody);
              resolve(characterData.name);
            }
          });
        });
      };

      // Use Promise.all to fetch character details in parallel
      Promise.all(movieData.characters.map(fetchCharacterDetails))
        .then(characterNames => {
          // Print character names one by one in the same order as the list in /films/ response
          characterNames.forEach(name => console.log(name));
        })
        .catch(fetchError => console.error(fetchError));
    } else {
      console.error(`Error: ${response.statusCode} - ${movieData.detail}`);
    }
  }
});
