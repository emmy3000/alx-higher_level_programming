#!/usr/bin/node
/*
 * function returns a reversed version of a list.
 * Use of the built-in method reverse() is forbidden.
 *
 */

exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;
    start++;
    end--;
  }

  return list;
};
