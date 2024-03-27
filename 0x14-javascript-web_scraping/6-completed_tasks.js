#!/usr/bin/node
// computes the number of task completed by user Id

const request = require('request');

const options = {
  url: process.argv[2],
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const done = {};
    data.forEach((task) => {
      if (task.completed && done[task.userId]) {
        done[task.userId] += 1;
      } else if (task.completed) {
        done[task.userId] = 1;
      }
    });
    console.log(done);
  }
}
request(options, callback);
