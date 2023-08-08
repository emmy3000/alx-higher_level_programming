#!/usr/bin/node
/**
 * Fetches and prints translations of "Hello" based on the entered language code.
 * Translation is triggered by clicking the button or pressing Enter on the input field.
 */
$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keyup', function (event) {
    if (event.type === 'click' || (event.type === 'keyup' && event.keyCode === 13)) {
      const languageCode = $('#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
