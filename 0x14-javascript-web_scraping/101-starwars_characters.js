#!/usr/bin/node
/**
 * Print all characters of a Star Wars movie by Movie ID.
 * Display one character name per line in the same order
 * as the list "characters" in the /films/ response.
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
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    let count = 0;

    const printCharacterName = (characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error while making the API request: ${error.message}`);
        } else if (response.statusCode !== 200) {
          console.error(`Failed to fetch data. Status Code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
          count++;
          if (count === characters.length) {
            // All character names have been printed, exit the script.
            process.exit(0);
          }
        }
      });
    };

    // Print character names in the same order as they appear in the "characters" list.
    characters.forEach((characterUrl) => {
      printCharacterName(characterUrl);
    });
  }
});
