#!/usr/bin/node
/*
 * function that returns the number of occurrences
 * in a list.
 *
 */

function nbOccurences (list, searchElement) {
  let count = 0;
  for (const item of list) {
    if (item === searchElement) {
      count += 1;
    }
  }
  return count;
}

module.exports = nbOccurences;
