#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getCharacterNames () {
  try {
    const response = await requestPromise(url);
    if (response.statusCode !== 200) {
      console.log('Error code: ' + response.statusCode);
      return;
    }

    const characters = JSON.parse(response.body).characters;
    for (const characterUrl of characters) {
      try {
        const charResponse = await requestPromise(characterUrl);
        if (charResponse.statusCode === 200) {
          const character = JSON.parse(charResponse.body).name;
          console.log(character);
        } else {
          console.log('Error code: ' + charResponse.statusCode);
        }
      } catch (err) {
        console.log(err);
      }
    }
  } catch (err) {
    console.log(err);
  }
}

getCharacterNames();
