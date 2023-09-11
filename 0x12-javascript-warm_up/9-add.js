#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  return sum;
}

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

const sum = add(num1, num2);
console.log(sum);
