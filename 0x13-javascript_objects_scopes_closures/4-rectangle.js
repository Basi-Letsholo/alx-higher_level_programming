#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    if (typeof w === 'undefined' || typeof h === 'undefined') {
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
