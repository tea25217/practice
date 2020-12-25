'use strict';
const request = require('request');
request('https://www.google.com', (error, response, body) => {
  console.log(body);
});