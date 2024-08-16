#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let tmp;
  for (let y = 0; y < args.length; y++) {
    for (let x = 0; x < args.length; x++) {
      if (args[x] > args[x + 1]) {
        tmp = args[x];
        args[x] = args[x + 1];
        args[x + 1] = tmp;
      }
    }
  }
  console.log(args[args.length - 2]);
}
