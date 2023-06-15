#!/usr/bin/node
/*
 * script imports an array & computes a new array.
 * The map() method must be utilized in this implementation.
 * A new list must be created with each value equal to the initial list,
 * multiplied by the index in the list.
 *
 */

const list = require('./100-data').list;

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
