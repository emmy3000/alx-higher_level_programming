#!/usr/bin/node
/**
 * Update the text color of the <header> element to red (#FF0000)
 * when the user clicks on the tag DIV#red_header.
 */
$(document).ready(function() {
	$('#red_header').click(function() {
		$('header').css('color', '#FF0000');
	});
});
