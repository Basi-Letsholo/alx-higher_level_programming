#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');

const url = args[1];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
