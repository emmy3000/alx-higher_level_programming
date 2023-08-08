#!/usr/bin/node
/**
 * Handles adding, removing, and clearing LI elements from a list.
 */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    const listItems = $('.my_list li');
    if (listItems.length > 0) {
      listItems.last().remove();
    }
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
