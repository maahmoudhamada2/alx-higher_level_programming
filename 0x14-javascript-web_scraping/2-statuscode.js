#!/usr/bin/node
// Script that display the status code of a GET request

const request = require('request');
const args = process.argv.slice(2);

const url = args[0];

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
