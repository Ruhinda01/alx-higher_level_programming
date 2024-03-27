#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars (characters, i) {
  request(characters[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i < characters.length - 1) {
        printChars(characters, i + 1);
      }
    }
  });
}
