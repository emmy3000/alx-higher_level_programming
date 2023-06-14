#!/usr/bin/node
/*
 * class Square inheriting features from class in module 5-square.js.
 * Class notation `extends` must be utilized for inheritance.
 * Create instance method charPrint(c) for printing the rectangle using
 * the character c.
 * If c is undefinded, use the character X in its place.
 *
 */

const Square = require('./5-square');

class ImprovedSquare extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    c = c || 'X';

    const line = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = ImprovedSquare;
