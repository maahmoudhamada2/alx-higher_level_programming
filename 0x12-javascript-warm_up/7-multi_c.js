#!/usr/bin/node
// script that prints x times “C is fun”

const args = process.argv.slice(2);

if (!Number.isNaN(Number.parseInt(args[0]))) {
  for (let i = 0; i < Number.parseInt(args[0]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
