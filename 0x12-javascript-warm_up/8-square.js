#!/usr/bin/node
// Script that prints a square

const args = process.argv.slice(2);
const num = Number.parseInt(args[0]);
if (!Number.isNaN(num)) {
  for (let x = 0; x < num; x++) {
    for (let y = 0; y < num; y++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
