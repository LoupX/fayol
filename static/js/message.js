/*
* Notifications for user's errors
* append a div into first place of the body and calculate the center of the document
* message_show receive 2 parameters, the first one is a css class and the next one is the message error.
*
*
*/
jQuery('body').prepend("<div id='fondo'><div id='mensaje' class='grid_4 text-center'> </div></div>");

var h   = (jQuery(document).height()/2)-100,
    w   = (jQuery(document).width()/2)-150,
    men = jQuery('#mensaje'),
    fon = jQuery('#fondo'),
    btn = jQuery('#btn');


function message_show(c, m) {
    var m = m,
        c = c;
	men.css({'margin-left': w, 'margin-top': h});
    fon.fadeIn("fast");
	men
        .addClass(c)
        .html('')
        .prepend(m+"<br><br><input id='btn' type='button' style='width:90%;' value='Aceptar'>")
		.stop(true)
		.effect("puff", { mode: 'show', percent: 50 }, 200)
		.effect("bounce", { mode: 'show', distance: 25, times: 6, direction: 'down'}, 200);
		//.effect("puff", { mode: 'show', percent: 50 }, 300);

    btn.live('click',function(){
        fon.fadeOut('fast');
        men
            .slideUp( function() {})
            .removeClass(c);
    });
}