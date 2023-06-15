#!/usr/bin/node
/*
 * script imports a dictionary of occurrences by user id and computes
 * a dictionary of user ids by occurrence.
 * key === number, while the value === user ids
 * Prints a new dictionary at the end.
 *
 */

const dict = require('./101-data').dict;

const newDict = {};
for (const userID in dict) {
  const occurrences = dict[userID];
  if (occurrences in newDict) {
    newDict[occurrences].push(userID);
  } else {
    newDict[occurrences] = [userID];
  }
}

console.log(newDict);
