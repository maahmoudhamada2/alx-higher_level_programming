#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const args = process.argv.slice(2);
const num = Number.parseInt(args[0]);

if (!Number.isNaN(num)) {
  const fact = factorial(num);
  console.log(fact);
} else {
  console.log(1);
}
