#!/usr/bin/node
/**
 * Fetches and prints translations of "Hello" based on the entered language code.
 */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
