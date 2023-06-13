#!/usr/bin/node
/* script that prints a message depending of the number of arguments passed */

const argsLength = process.argv.length;

if (argsLength === 2) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
