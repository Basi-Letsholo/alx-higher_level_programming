#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      str = '';
      for (let j = 0; j < this.size; j++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
