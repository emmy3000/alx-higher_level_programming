#!/usr/bin/node
/*
 * updated script by adding a new function incr()
 * that increments the integer value.
 *
 */

const myObject = {
  type: 'object',
  value: 12,
  incr: function incr () {
    this.value++;
  }
};

delete myObject.incr;

console.log(myObject);
myObject.incr = function () {};
myObject.incr();
console.log(myObject);
myObject.incr = function () {};
myObject.incr();
console.log(myObject);
myObject.incr = function () {};
myObject.incr();
console.log(myObject);
