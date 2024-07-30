#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
}
);
