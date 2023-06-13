#!/usr/bin/node
/*
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer.
 *
 */

const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
