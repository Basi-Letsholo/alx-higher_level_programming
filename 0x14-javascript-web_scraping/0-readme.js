#!/usr/bin/node

const args = process.argv.slice(1)
const fs = require('fs')

const file_path = args[1]

fs.readFile(file_path, 'utf8', (err, data) => {
	if (err) throw err;
	console.log(data.toString());
});
