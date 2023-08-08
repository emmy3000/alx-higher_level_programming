#!/usr/bin/node
/**
 * Fetches and lists the titles for all movies from the given URL
 * and displays them in the UL#list_movies tag.
 */
const $ = window.$;
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const listElement = $('#list_movies');
    for (const movie of movies) {
      $('<li>').text(movie.title).appendTo(listElement);
    }
  });
});
