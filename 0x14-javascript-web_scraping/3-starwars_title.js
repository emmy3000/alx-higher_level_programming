#!/usr/bin/node
/**
 * Print the title of the Star Wars movie with the given episode number.
 */
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error while making the API request: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status Code: ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    console.log(`Title: ${movie.title}`);
  }
});
