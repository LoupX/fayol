function message() {
	jQuery('#fondo').fadeIn("fast");
	jQuery("#mensaje")
		.stop(true)
		.effect("puff", { mode: 'show', percent: 50 }, 200)
		.effect("bounce", { mode: 'show', distance: 25, times: 6, direction: 'down'}, 200);
		//.effect("puff", { mode: 'show', percent: 50 }, 300);
}