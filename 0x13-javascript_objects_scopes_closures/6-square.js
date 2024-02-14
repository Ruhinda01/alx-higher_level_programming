#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let r = 0; r < this.height; r++) {
      let shp = '';
      for (let h = 0; h < this.width; h++) {
        shp += c;
      }
      console.log(shp);
    }
  }
}

module.exports = Square;
