#!/usr/bin/node

const request = require('require');

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/`;

request(apiUrl + id, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    } else {
      console.error(`Error: ${response.statusCode} - ${movieData.detail}`);
    }
  }
});
