#!/usr/bin/node
// Function that increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  let count = 1;
  for (let x = 0; x < number; x++) {
    count++;
  }
  theFunction(count);
};
