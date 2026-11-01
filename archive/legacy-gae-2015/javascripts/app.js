'use strict';

$(function () {
	
	var pull 		= $('#pull');
	var menu 		= $('nav ul');
	var menuHeight	= menu.height();

	$(pull).on('click', function(e) {
		e.preventDefault();
		menu.slideToggle();
	});

	$(window).resize(function(){
		var w = $(window).width();
		if(w > 320 && menu.is(':hidden')) {
			menu.removeAttr('style');
		}
	});
	
	$('#number').focusout(function () {
		var number = $('#number').val();
		var type = getCreditCardType(number);
		var length = $('#type').val().length;
		if (type !== "unknown" && length === 0) {
			$('#type').val(type);
		}
	}); 
});