#!/usr/bin/node

function factorial (number) {
  if (number <= 1) {
    return 1;
  }

  const result = number * factorial(number - 1);
  return result;
}

const args = process.argv;
const num = parseInt(args[2], 10);

if (isNaN(num)) {
  console.log(1);
} else {
  const numFactorial = factorial(num);
  console.log(numFactorial);
}
