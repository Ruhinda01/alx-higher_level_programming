#!/usr/bin/node

const request = require('request');

const options = {
    url: process.argv[2],
    headers: {
        'User-Agent': 'request'
    }
};

function callback(error, response, body) {
    if (!error && response.statusCode === 200) {
        const data = JSON.parse(body).results
        let count = 0;
        for (let i = 0; i < data.length; i++) {
            for (let j = 0; j < data[i].characters.length; j++) {
                if (data[i].characters[j].includes('/18/')) {
                    count += 1;
                }
            }
        }
        console.log(count);
    }
}
request(options, callback);
