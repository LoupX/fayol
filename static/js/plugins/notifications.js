var Messages = {
    merror: "Ocurrió un error con los datos del formulario.",
    msuccess: "Se han guardado los datos del formulario.",
    mexists: "Ese proveedor existe, para editarlo vaya a la sección de ver proveedor.",
    malert: "Verifique los datos antes de guardar, posteriormente no se podrán editar.",
    nspeed: 600,
    sspeed: 1700,
    scroll: 1000,
    showM: function(which, phrase, speed) {
            speed = (speed) ? speed: 600;

            phrase = this.whichMessage(which, phrase);

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
        jQuery('body','html', window, document).animate( {scrollTop: 0}, this.scroll);
    }
    ,
    hideAll: function() {
        jQuery('.msgerror, .msgsuccess, .exists').hide();
    }
    ,
    successWR: function(which, url, speed, phrase) {
        speed = (speed) ? speed: this.sspeed;

        phrase = this.whichMessage(which, phrase);

        jQuery(which+' p').html(phrase);
        jQuery(which).fadeIn(speed, function() {
            window.location.replace(url);
        });
        this.scrollPage();
    },
    whichMessage: function(which, phrase) {
        switch(which) {
                case '.msgsuccess':
                    phrase = (phrase) ? phrase: this.msuccess;
                    break;
                case '.msgerror':
                    phrase = (phrase) ? phrase: this.merror;
                    break;
                case '.exists':
                    phrase = (phrase) ? phrase: this.mexists;
                    break;
                case '.msgalert':
                    phrase = (phrase) ? phrase: this.malert;
                    break;
        }

        return phrase;
    },
    version: 'v0.1.1'
}