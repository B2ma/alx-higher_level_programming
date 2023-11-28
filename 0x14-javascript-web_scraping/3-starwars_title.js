#!/usr/bin/node

const request = require('require');

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    if (response.statusCode === 200) {
      console.log(movieData.title);
    } else {
      console.error(`Error: ${response.statusCode} - ${movieData.detail}`);
    }
  }
});
