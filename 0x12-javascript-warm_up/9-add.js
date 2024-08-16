#!/usr/bin/node
// script that prints the addition of 2 integers

function add (a, b) {
  return Number.parseInt(a) + Number.parseInt(b);
}

const args = process.argv.slice(2);
const result = add(args[0], args[1]);

console.log(result);
