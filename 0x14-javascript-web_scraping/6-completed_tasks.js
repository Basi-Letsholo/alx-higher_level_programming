#!/usr/bin/node

const args = process.argv.slice(1);
const request = require('request');

const url = args[1];

request(url, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  const tasksDone = {};
  for (const task of data) {
    if (task.completed) {
      tasksDone[task.userId] = (tasksDone[task.userId] || 0) + 1;
    }
  }
  console.log(tasksDone);
});
