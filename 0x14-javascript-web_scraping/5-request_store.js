#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');

const url = args[0];
const filePath = args[1];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  }
  );
}
);
