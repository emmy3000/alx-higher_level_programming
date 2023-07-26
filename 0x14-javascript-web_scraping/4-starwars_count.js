#!/usr/bin/node
/**
 * Print the number of movies where the character "Wedge Antilles" is present.
 */
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error while making the API request: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status Code: ${response.statusCode}`);
  } else {
    const movies = JSON.parse(body).results;
    const moviesWithWedgeAntilles = movies.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(`${moviesWithWedgeAntilles.length}`);
  }
});
