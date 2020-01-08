var planetarium8;
S(document).ready(function() {
	planetarium8 = S.virtualsky({
		'id': 'starmap8',
		'projection': 'gnomic',
		'ra': 83.8220833,
		'dec': -5.3911111,
		'ground': false,
		'constellations': true,
		'constellationlabels': true,
		'gridlines_gal': true,
		'fov': 15,
		'callback': {
			'contextmenu': function(e){
				console.log('contextmenu callback', e);
				if(e.ra && e.dec){
planetarium8.addPointer({
	ra: e.ra,
	dec: e.dec,
	label: "Clicked here",
	colour: "#ffffff",
});
planetarium8.draw();
				}
			},
			'click': function(e){
				e.nearest = e.data.sky.nearestObject(e.x,e.y);
				console.log(e.nearest,e.ra,e.dec);
			}
		}
	});

	S('button#orion').on('click',function(){ planetarium8.panTo(86,6,3000); });
	S('button#capricornus').on('click',function(){ planetarium8.panTo(150,140,3000); });
	S('button#scorpius').on('click',function(){ planetarium8.panTo(83.6330833,22.0145000,3000); });
	S('button#ursamajor').on('click',function(){ planetarium8.panTo(83.8220833,-5.3911111,3000); });

});
