#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”

const args = process.argv.slice(2);
const fullPhrase = args[0] + ' is ' + args[1];

console.log(fullPhrase);
