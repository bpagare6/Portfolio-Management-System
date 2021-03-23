
$(document).ready(function() {
	'use strict';

  $('.test-step .button').on('click', function(e) {
  	e.preventDefault();
    $(this).parents('.test-step').next().addClass('active');
    $(this).parents('.test-step').removeClass('active');
  })

  $('.test-step .prev-btn').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.test-step').prev().addClass('active');
    $(this).parents('.test-step').removeClass('active');
  })

})
