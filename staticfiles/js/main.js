/*
	Epilogue by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

(function($) {

	skel.breakpoints({
		xlarge: '(max-width: 1680px)',
		large: '(max-width: 1280px)',
		medium: '(max-width: 980px)',
		small: '(max-width: 736px)',
		xsmall: '(max-width: 480px)',
		xxsmall: '(max-width: 360px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

		// Items.
			$('.item').each(function() {

				var $this = $(this),
					$header = $this.find('header'),
					$a = $header.find('a'),
					$img = $header.find('img');

				// Set background.
					$a.css('background-image', 'url(' + $img.attr('src') + ')');

				// Remove original image.
					$img.remove();

			});


			

	});

})(jQuery);


// // https://ultimatedjango.com/learn-django/lessons/newedit-contact-enable-ajax-2/?trim=yes
// $(document).ready(function() {

// // Account - Use AJAX to get the Account Edit form and
// // display it on the page w/out a refresh
// $('#gi-container').delegate('.edit-account', 'click', function(e) {
//     e.preventDefault();
//     $('#gi-container').load($(this).attr('href'));
// });



// //https://ultimatedjango.com/learn-django/lessons/newedit-contact-enable-ajax/?trim=yes
// // Contact - Use AJAX to get the Contact Add form
// $('#cd-container').delegate('#new-contact', 'click', function(e) {
//     e.preventDefault();
//     $.get($(this).attr('href'), function(data) {
//         $('#cd-body').append(data);
//         $('#new-contact').hide();
//     });
// });

// // Contact - Use AJAX to get the Contact Edit form
// $('#cd-container').delegate('.edit-contact', 'click', function(e) {
//     e.preventDefault();
//     var that = $(this);
//     $.get($(this).attr('href'), function(data) {
//         $('#new-contact').hide();
//         that.parent().parent().remove();
//         $('#cd-body').append(data);
//     })
// });

// // Contact - Use AJAX to save the Contact Add Form
// $('#cd-container').delegate('#contact-form', 'submit', function(e) {
//     e.preventDefault();
//     var form = $('#contact-form');
//     var url = form.attr('action');
//     $.post(url, form.serialize(), function(data) {
//         if ($(data).find('.errorlist').html()) {
//             // If the contact form is returned we know there are errors
//             $('#new-contact').hide();
//             $('#cd-body').append(data);
//         } else {
//             // Otherwise insert the row into the table
//             $('#cd-table tr:last').after(data);
//             $('#new-contact').show();
//         }
//     });
//     $(this).remove(); // Remove the form
// });

// // https://ultimatedjango.com/learn-django/lessons/newedit-comm-enable-ajax/?trim=yes
// // Communications - When the Subject of the form is clicked, the whole form is displayed
//     $('#co-container').delegate('#id_subject', 'focus', function() {
//         $('#comm-form-internals').show();
//     });


//     // Communications - Use AJAX to get the Communications Add Form
//     $('#co-container').delegate('#new-comm', 'click', function(e) {
//         e.preventDefault();
//         $.get($(this).attr('href'), function(data) {
//             $('#co-list').prepend(data);
//         })
//     });


//     // Communications - Use AJAX to get the Comm Edit Form
//     $('#co-container').delegate('.comm-edit', 'click', function(e) {
//         e.preventDefault();
//         var that = $(this);
//         $.get($(this).attr('href'), function(data) {
//             $('#co-body').find('#comm-form').remove();
//             $('#co-form-wrapper').append(data);
//             $('#comm-form-internals').show();
//             that.parent().parent().parent().remove();
//         })
//     });


//     // Communications - Use AJAX to save the Comm Add Form
//     $('#co-container').delegate('#comm-form', 'submit', function(e) {
//         e.preventDefault();
//         var form = $('#comm-form');
//         var url = form.attr('action');
//         $.post(url, form.serialize(), function(data) {
//             if ($(data).find('#comm-form-internals').html()) {
//                 // If form comes back then display it properly
//                 form.remove();
//                 $('#co-form-wrapper').prepend(data); // Appends the newly created Communication
//                 $('#comm-form-internals').show(); // Make sure it shows
//                 $('#comm-form').attr('action', '/comm/new/'); // Make sure the action is set to new
//             } else {
//                 // When is this supposed to kick in?
//                 resetForm($('#comm-form')); // Resets the form values
//                 $('#comm-form').find('ul').remove(); // If there are any errors on the form, remove them all
//                 $('#comm-form-internals').hide(); // Hides everything but the subject
//                 $('#co-list').prepend(data); // Appends the newly created Communication
//                 $('#comm-form').attr('action', '/comm/new/'); // Make sure the action is set to new
//             }
//         })
//     });




// });