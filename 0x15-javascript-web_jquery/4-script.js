#!/usr/bin/node
/**
 * Toggle the class of the <header> element between 'red' and 'green'
 * when the user clicks on DIV#toggle_header.
 */
const $ = window.$;
$(document).ready(function() {
  $('DIV#toggle_header').on('click', function() {
    $('header').toggleClass('red green');
  });
});
