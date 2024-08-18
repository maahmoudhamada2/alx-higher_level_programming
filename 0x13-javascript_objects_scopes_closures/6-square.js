#!/usr/bin/node
// Class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const origSquare = require('./5-square.js');

module.exports = class Square extends origSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let h = 0; h < this.height; h++) {
        for (let w = 0; w < this.width; w++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
