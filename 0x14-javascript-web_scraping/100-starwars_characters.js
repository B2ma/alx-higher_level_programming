#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {

    const movieData = JSON.parse(body);

    if (response.statusCode === 200) {
      movieData.characters.forEach(characterUrl => {
        request(characterUrl, function (characterError, characterResponse, characterBody) {
          if (characterError) {
            console.error(characterError);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          }
        });
      });
    } else {
      console.error(`Error: ${response.statusCode} - ${movieData.detail}`);
    }
  }
});
