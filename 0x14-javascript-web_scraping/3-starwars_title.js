#!/usr/bin/node

const request = require('require');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    if (response.statusCode === 200) {
      console.log(movieData.title);
    }
  }
});
