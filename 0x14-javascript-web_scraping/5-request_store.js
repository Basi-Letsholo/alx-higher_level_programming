#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');
const fs = require('fs');

const url = args[1];
const filePath = args[2];

request(url, (error, response, body) => {
  if (error) console.error(error);

  const data = body;
  fs.writeFile(filePath, data, 'utf8', (err) => {
    if (err) throw err;
  });
});
