#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const myJson = JSON.parse(body);
  const result = myJson.results;
  for (let i = 0; i < result.length; i++) {
    const chars = result[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j] === charUrl) {
        count++;
      }
    }
  }
  console.log(count);
}
);
