#!/usr/bin/node

const args = process.argv.slice(1);
const fs = require('fs');

const filePath = args[1];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
