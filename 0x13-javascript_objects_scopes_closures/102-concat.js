#!/usr/bin/node
/*
 * Script concats two files.
 * first arg: file path of the first source file.
 * second arg: file path of the seconf source file.
 * third arg: file path of the destination.
 *
 */

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destination = process.argv[4];

const content =
  fs.readFileSync(sourceFile1, 'utf-8') + fs.readFileSync(sourceFile2, 'utf-8');
fs.writeFileSync(destination, content, { encoding: 'utf-8' });
