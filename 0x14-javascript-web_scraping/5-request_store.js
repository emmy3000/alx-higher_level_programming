#!/usr/bin/node
/**
 * Make a GET request to the specified URL and store the response in a file.
 */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error while making the request: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status Code: ${response.statusCode}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error while writing to the file: ${err.message}`);
      } else {
        console.log(`${filePath}`);
      }
    });
  }
});
