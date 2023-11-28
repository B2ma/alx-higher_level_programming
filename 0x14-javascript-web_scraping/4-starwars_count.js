#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Filter films where "Wedge Antilles" is present
    const filmsWithWedge = filmsData.results.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    // Print the number of movies
    console.log(filmsWithWedge.length);
  }
});
