#!/usr/bin/node

const args = process.argv.slice(1);
const fs = require('fs');

const filePath = args[1];
const toWrite = args[2];

fs.writeFile(filePath, toWrite, 'utf8', (err) => {
  if (err) throw err;
 });
