#!/usr/bin/node
/**
 * Fetches the character name from the given URL and displays it in the DIV#character tag.
 */
const $ = window.$;
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
