#!/usr/bin/node
/**
 * Add a new <li> element to UL.my_list when the user clicks on DIV#add_item.
 */
const $ = window.$;
$(document).ready(function() {
  $('DIV#add_item').on('click', function() {
    $('ul.my_list').append('<li>Item</li>');
  });
});
