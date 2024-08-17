#!/usr/bin/node
// Function that returns the reversed version of a list

exports.esrever = function (list) {
  const revArr = [];

  for (let x = list.length - 1, y = 0; x >= 0; x--, y++) {
    revArr[y] = list[x];
  }
  return revArr;
};
