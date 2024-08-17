#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const args = process.argv.slice(2);

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
