#!/usr/bin/node
/* script that prints the addition of 2 integers */

function add (a, b) {
  return a + b;
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
const result = add(num1, num2);

console.log(result);
