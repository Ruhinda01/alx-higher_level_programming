#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const file_name = process.argv[3];
const url = process.argv[2];

request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        fs.writeFile(file_name, body, 'utf8', (err) => {
            if (err) {
                console.log(err);
            }
        });
    }
});
