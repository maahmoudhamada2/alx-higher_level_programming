#!/usr/bin/node
// Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const args = process.argv.slice(2);

if (!Number.isNaN(Number.parseInt(args[0]))) {
  console.log('My number:', Number.parseInt(args[0]));
} else {
  console.log('Not a number');
}
