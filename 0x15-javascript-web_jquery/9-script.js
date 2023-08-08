#!/usr/bin/node
/**
 * Fetches translation of "hello" from a specific URL and displays it in the DIV#hello tag.
 */
const $ = window.$;
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
