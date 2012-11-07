var Messages = {
    merror: "something was wrong",
    msuccess: "something was right",
    mexists: "something exists",
    malert: "be careful",
    showM: function(which, phrase, speed) {
            speed = (speed) ? speed: 600;
            jQuery(which+' p').html(phrase);
            jQuery(which).fadeIn(speed);
            this.scrollPage();
    },
    hideM: function(which) {
            jQuery(which).hide();
            this.scrollPage();
    },
    setPhrases: function() {
        jQuery('.msgerror p').html(this.merror);
        jQuery('.msgsuccess p').html(this.msuccess);
        jQuery('.exists p').html(this.mexists);
        jQuery('.msgalert p').html(this.malert);
    },
    scrollPage: function() {
        jQuery('body','html', window, document).animate( {scrollTop: 0}, 1000);
    }
    ,
    hideAll: function() {
        jQuery('.msgerror, .msgsuccess, .exists').hide();
    }
    ,
    successWR: function(which, phrase, speed, url) {
        speed = (speed) ? speed: 1600;
        jQuery(which+' p').html(phrase);
        jQuery(which).fadeIn(speed, function() {
            window.location.replace(url);
        });
        this.scrollPage();
    },
    version: 'v0.1'
}