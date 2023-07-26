#!/usr/bin/node
/**
 * Read and print the content of a file specified as an argument.
 * If an error occurs during reading, the error message will be printed.
 */
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.error(`Error reading the file: ${err.message}`);
    return;
  }
  console.log(data);
});
