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
			.attr('placeholder','No puedes dejar vacio este campo')
			.removeClass('input_usr')
			.addClass('usr_error');
			b_u = false;
	} 
	else 
		{
		usr
			.attr('placeholder','Usuario')
			.removeClass('usr_error')
			.addClass('input_usr');
		b_u = true;
	}

	if ( pwd.val() == "" ) 
	{
		//usr.css({border: '2px solid #e84141'});
		pwd
			.attr('placeholder','No puedes dejar vacio este campo')
			.removeClass('input_pwd')
			.addClass('pwd_error');
			b_p = false;
	} 
	else 
		{
		pwd
			.attr('placeholder','Contraseña')
			.removeClass('pwd_error')
			.addClass('input_pwd');
		b_p = true;
	}

	//console.log(b_u+''+b_p);
	if( b_u  && b_p ) { bol = true; } else { bol = false; }		
	return bol
}