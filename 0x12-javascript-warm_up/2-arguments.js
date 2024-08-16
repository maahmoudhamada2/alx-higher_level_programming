#!/usr/bin/node
// script that prints a message depending of the number of arguments passed

const args = process.argv.slice(2);
const argsCount = args.length;
if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
