#!/usr/bin/node
/*
 * Script concats two files.
 * first arg: file path of the first source file.
 * second arg: file path of the seconf source file.
 * third arg: file path of the destination.
 *
 */

const fs = require('fs');

/* Check if all command-line arguments are provided */
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

/* Read the contents of the first file */
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}: ${err.message}`);
    process.exit(1);
  }

  /* Read the contents of the second file */
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}: ${err.message}`);
      process.exit(1);
    }

    /* Concatenate the contents of the two files with a newline */
    const concatenatedData = `${data1.trim()}\n${data2.trim()}\n`;

    /* Write the concatenated data to the destination file */
    fs.writeFile(destination, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destination}: ${err.message}`);
        process.exit(1);
      }

      console.log(`${file1} and ${file2} have been concatenated into ${destination}`);
    });
  });
});
