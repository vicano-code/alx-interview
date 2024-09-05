#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const result = [];
    result.push(body);
    r = JSON.parse(result);
    console.log(result);
    for (const i in r.characters) {
      request(r.characters[i], function (err, response, body) {
        if (err) {
	  console.log(err);
        }
        if (response.statusCode === 200) {
	  console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
