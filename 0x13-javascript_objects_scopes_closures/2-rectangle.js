#!/usr/bin/node
/*
 * class constructor intializing attributes and creates
 * an empty object if attribute value is <= 0.
 *
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
