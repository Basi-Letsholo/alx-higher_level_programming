#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');
const util = require('util');
const promisifyRequest = util.promisify(request);

const movieId = parseInt(args[1], 10);
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const fetchCharacter = async (charUrl) => {
  try {
    const charData = await promisifyRequest(charUrl);
    const parsedCharData = JSON.parse(charData.body);
    console.log(parsedCharData.name);
  } catch (err) {
    console.error(err);
  }
};

(async () => {
  try {
    const movieData = await promisifyRequest(url);
    const parsedMovieData = JSON.parse(movieData.body);
    const charUrls = parsedMovieData.characters;

    const idList = [];
    for (const charId of charUrls) {
      const match = charId.match(/\d+/);
      if (match) {
        const foundId = parseInt(match[0], 10);
        idList.push(foundId);
      }
    }

    idList.sort((a, b) => a - b);

    for (const num of idList) {
      const charUrl = 'https://swapi-api.alx-tools.com/api/people/' + num;
      await fetchCharacter(charUrl);
    }
  } catch (err) {
    console.error(err);
  }
})();
