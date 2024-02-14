#!/usr/bin/mode

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let r = 0; r < this.height; r++) {
      let sqr = '';
      for (let c = 0; c < this.width; c++) {
        sqr += 'X';
      }
      console.log(sqr);
    }
  }
}

module.exports = Rectangle;
