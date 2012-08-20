var pce = jQuery('#placeholder_empty').val(),
    pus = jQuery('#placeholder_user').val(),
    ppa = jQuery('#placeholder_pass').val();

function validate(usr, pwd, tkn) {
	var usr = usr, //jQuery('#usr'),
		pwd = pwd, //jQuery('#pwd'),
		tkn = tkn, //jQuery('div.hidden input').val(),
		b_u = false,
		b_p = false,
		bol = null;

	if ( usr.val() == "" ) 
	{
		//usr.css({border: '2px solid #e84141'});
		usr
			.attr('placeholder',pce)
			.removeClass('input_usr')
			.addClass('usr_error');
			b_u = false;
	} 
	else 
		{
		usr
			.attr('placeholder',pus)
			.removeClass('usr_error')
			.addClass('input_usr');
		b_u = true;
	}

	if ( pwd.val() == "" ) 
	{
		//usr.css({border: '2px solid #e84141'});
		pwd
			.attr('placeholder',pce)
			.removeClass('input_pwd')
			.addClass('pwd_error');
			b_p = false;
	} 
	else 
		{
		pwd
			.attr('placeholder',ppa)
			.removeClass('pwd_error')
			.addClass('input_pwd');
		b_p = true;
	}

	//console.log(b_u+''+b_p);
	if( b_u  && b_p ) { bol = true; } else { bol = false; }		
	return bol
}