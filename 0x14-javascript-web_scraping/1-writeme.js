#!/usr/bin/node
const fs = require('fs');
/**
 * Write a string to a file specified by the file path.
 * If an error occurs during writing, the error message will be printed.
 */
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(`Error writing to the file: ${err.message}`);
  } else {
    console.log('Content has been successfully written to the file.');
  }
});
