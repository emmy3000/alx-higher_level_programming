#!/usr/bin/node
/*
 * Creating two instance methods.
 * rotate(): used in exchanging the width and rectangle.
 * double(): multiplies the width and height of the rectangle by 2.
 *
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; /* Create an empty object if w or h is 0 or not a positive integer */
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width]; /* Swap width and height */
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
