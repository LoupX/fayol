/*
* Notifications for user's errors
* append a div into first place of the body and calculate the center of the document
* message_show receive 2 parameters, the first one is a css class and the next one is a message error.
*
*
*/
jQuery('body').prepend("<div id='mensaje' class='grid_4 text-center'> </div>");

var h   = (jQuery(document).height()/2)-100,
    w   = (jQuery(document).width()/2)-150,
    men = jQuery('#mensaje'),
    //fon = jQuery('#fondo'),
    btn = jQuery('#btn'),
    ste = jQuery('#btn_enter').val();

function message_show(c, m) {
    var m = m,
        c = c;
	men.css({'margin-left': w});
    //fon.fadeIn("fast");
	men
        .addClass(c)
        .html('')
        .prepend(m+'<br><br><input id="btn" type="button" style="width:90%;" value="'+ste+'">')
		.stop(true)
        .slideDown();
		//.effect("puff", { mode: 'show', percent: 50 }, 200)
		//.effect("bounce", { mode: 'show', distance: 25, times: 6, direction: 'down'}, 200);
		//.effect("puff", { mode: 'show', percent: 50 }, 300);
    jQuery('#btn').focus();

    btn.live('click',function(){
        //if the button is pressed hide the message
        men
            .slideUp()
            .removeClass(c);
    });

    men.bind('keydown', 'enter', function() {
        //if the intro key is pressed hide the message;
        men
            .slideUp( function() {})
            .removeClass(c)
            .hide();
        men.unbind();
    });
}