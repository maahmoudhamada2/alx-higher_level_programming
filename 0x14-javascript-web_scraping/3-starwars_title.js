#!/usr/bin/node

const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = args[0];
const request = require('request');
const fullUrl = url + id;

request(fullUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const myJson = JSON.parse(body);
  console.log(myJson.title);
}
);
