#!/usr/bin/node
/*
 * function prints the number of arguments already printed and the new argument
 * value.
 * Output format: <number arguments already printed>: <current argumentvalue>
 *
 */

let numArguments = 0;

exports.logMe = function (item) {
  console.log(`${numArguments}: ${item}`);
  numArguments++;
};
