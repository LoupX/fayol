/*
 * 	Additional function for forms.html
 *	Written by ThemePixels	
 *	http://themepixels.com/
 *
 *	Copyright (c) 2012 ThemePixels (http://themepixels.com)
 *	
 *	Built for Amanda Premium Responsive Admin Template
 *  http://themeforest.net/category/site-templates/admin-templates
 */

jQuery(document).ready(function(){
	
	///// DUAL BOX CATEGORIES/////
	var db = jQuery('#dualselect_categories').find('.ds_arrow .arrow');	//get arrows of dual select
	var sel1 = jQuery('#dualselect_categories select:first-child');		//get first select element
	var sel2 = jQuery('#dualselect_categories select:last-child');			//get second select element
	
	sel2.empty(); //empty it first from dom.
	
	db.click(function(){
		var t = (jQuery(this).hasClass('ds_prev'))? 0 : 1;	// 0 if arrow prev otherwise arrow next
		if(t) {
			sel1.find('option').each(function(){
				if(jQuery(this).is(':selected')) {
					jQuery(this).attr('selected',false);
					var op = sel2.find('option:first-child');
					sel2.append(jQuery(this));
				}
			});	
		} else {
			sel2.find('option').each(function(){
				if(jQuery(this).is(':selected')) {
					jQuery(this).attr('selected',false);
					sel1.append(jQuery(this));
				}
			});		
		}
	});
	
	
		///// DUAL BOX VENDORS/////
	var db = jQuery('#dualselect_vendors').find('.ds_arrow .arrow');	//get arrows of dual select
	var sel3 = jQuery('#dualselect_vendors select:first-child');		//get first select element
	var sel4 = jQuery('#dualselect_vendors select:last-child');			//get second select element
	
	sel4.empty(); //empty it first from dom.
	
	db.click(function(){
		var t = (jQuery(this).hasClass('ds_prev'))? 0 : 1;	// 0 if arrow prev otherwise arrow next
		if(t) {
			sel3.find('option').each(function(){
				if(jQuery(this).is(':selected')) {
					jQuery(this).attr('selected',false);
					var op = sel4.find('option:first-child');
					sel4.append(jQuery(this));
				}
			});	
		} else {
			sel4.find('option').each(function(){
				if(jQuery(this).is(':selected')) {
					jQuery(this).attr('selected',false);
					sel3.append(jQuery(this));
				}
			});		
		}
	});

});