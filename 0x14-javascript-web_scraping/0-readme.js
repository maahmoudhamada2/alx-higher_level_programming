#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');
const args = process.argv.slice(2);

fs.readFile(args[0], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
