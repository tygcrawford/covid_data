const url='http://localhost:5000';

$(document).ready( function() {
	$.get( url, function( r ) {
		let cd = JSON.parse(r);
		google.charts.load('current', {
	   		'packages':['geochart', 'corechart'],
	    	'mapsApiKey': 'AIzaSyDf56jExX-pA3hna6HDD3nAeHBJFD6mkEA'
	    });
	    google.charts.setOnLoadCallback(drawRegionsMap);

	    let dt = [['Country', 'Cases']];
	    for(var c in cd.countries){
	    	dt[dt.length] = [c, cd.countries[c].days[cd.countries[c].days.length-1].cases];
	    }

      	function drawRegionsMap() {
        	var data = google.visualization.arrayToDataTable(dt);


	    var options = {
        	colorAxis: {colors: ['#4D2424', '#ff0000']},
        	backgroundColor: '#1a1a1a',
        	datalessRegionColor: '#212121'
	    };

	    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

	    chart.draw(data, options);
      }
		
	});
});