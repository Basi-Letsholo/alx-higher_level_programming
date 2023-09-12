#!/usr/bin/node

function esrever (list) {
  const reverseList = [];

  if (list.length <= 0 || typeof list.length !== 'number') {
    return [];
  }

  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }

  return reverseList;
}

module.exports = {
  esrever
};
