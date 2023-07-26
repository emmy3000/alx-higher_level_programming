#!/usr/bin/node
/**
 * Make a GET request to the specified URL and display the status code.
 */
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(`Error while making the request: ${error.message}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
