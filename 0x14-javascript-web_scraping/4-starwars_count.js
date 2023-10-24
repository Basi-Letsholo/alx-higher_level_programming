#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');

const url = args[1];
const charId = 18;

request(url, (error, response, body) => {
  if (error) console.log(err);
	const num = body.split('/people/18').length;

	console.log(num - 1);
});
