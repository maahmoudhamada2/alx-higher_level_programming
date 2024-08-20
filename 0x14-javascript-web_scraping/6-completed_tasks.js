#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2)

request.get(args[0], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    for (let x = 0; x < body.length; x++) {
      console.log(body[x].completed)
    }
  }
});
