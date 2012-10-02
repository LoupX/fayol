
function validate_this_input(myinput_id) {
    var myinput_id  = jQuery('input[name="'+myinput_id+'"]'),
        bol         = false;

    if ( myinput_id.val() == "" )
    {
        myinput_id
            .removeClass('input_normal')
            .addClass('input_error');
        bol = false;
    }
    else
    {
        myinput_id
            .removeClass('input_error')
            .addClass('input_normal');
        bol = true;
    }

    return bol
}