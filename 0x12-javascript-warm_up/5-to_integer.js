#!/usr/bin/node

const args = process.argv;
const firstArg = parseInt(args[2], 10);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArg);
}
