#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');

const movieId = parseInt(args[1], 10);
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, response, body) => {
  if (err) console.error(err);

  const movieData = JSON.parse(body);
  const charUrls = movieData.characters;

  for (const character of charUrls) {
    request(character, (err, response, body) => {
      if (err) console.log(err);

      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
