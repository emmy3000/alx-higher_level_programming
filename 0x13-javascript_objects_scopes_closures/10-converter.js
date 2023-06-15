#!/usr/bin/node
/*
 * function that converts a number from base 10 to another base
 * passed as argument.
 *
 */

exports.converter = function (base) {
  if (base === 0) {
    return function (number) {
      return number.toString(base);
    };
  } else {
    return function (number) {
      return number.toString(base);
    };
  }
};
