#!/usr/bin/node

function secondBiggest (listInt) {
  if (listInt.length <= 1) {
    return 0;
  }

  let maxInt = listInt[0];
  for (let i = 0; i < listInt.length; i++) {
    if (listInt[i] > maxInt) {
      maxInt = listInt[i];
    }
  }

  const maxRemoved = listInt.filter(item => item !== maxInt);

  if (maxRemoved.length <= 0) {
    return 0;
  }

  let secondMax = maxRemoved[0];
  for (let i = 0; i < maxRemoved.length; i++) {
    if (maxRemoved[i] > secondMax) {
      secondMax = maxRemoved[i];
    }
  }

  return secondMax;
}

const args = process.argv;
const argsLen = args.length;
const intArray = [];

for (let i = 2; i < argsLen; i++) {
  intArray.push(parseInt(args[i]));
}

const secondMax = secondBiggest(intArray);

console.log(secondMax);
