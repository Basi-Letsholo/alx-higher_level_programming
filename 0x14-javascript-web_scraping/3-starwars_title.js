#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');

const movieId = parseInt(args[1], 10);
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error(error);
  }
});
