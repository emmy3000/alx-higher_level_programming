#!/usr/bin/node
/*
 * script that searches the second biggest integer
 * in the list of arguments.
 *
 */

function findSecondLargest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const current = parseInt(numbers[i]);

    if (current > largest) {
      secondLargest = largest;
      largest = current;
    } else if (current > secondLargest && current !== largest) {
      secondLargest = current;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2);
const result = findSecondLargest(args);

console.log(result);
