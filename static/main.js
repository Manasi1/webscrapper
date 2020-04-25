// This searches for a recipe and nutriotion values for it's ingredients
$("document").ready(function() {
		var s;
		var s1 = {};
		$.get('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic', function( html ) {
		
		
	   s = "<table><tr><td>Total Confirmed Cases</td><td>Total Deaths</td><td>Total Recovered Cases</td><td>Updated date</td></tr><tr>";
	   for(var i=0;i<3;i++)
	   {
		 $(html).find("#thetable").find("tbody").find("tr:eq(1)").find("th:eq("+(i+1)+")").each( function(){
			var test = $(this).text();
			//return test;
			s = s+ "<td>"+test+"</td>";
			s1[i]=test;
		});
		//s = s+ "<td>"+text+"</td>";
		
	   }

	   senddata(s1);
	   s=s+"<td>"+`${Date()}`.substr(4,11)+"</td></tr></table>";
		 $("#content").append(s);
		 console.log( JSON.stringify(s1) );
	var body = $(html).find("#covid19-container").find("table").find("tbody").html();
            $("#full").append(body);
	} )

	function senddata(data)
	{
		var request = new XMLHttpRequest()

	// Open a new connection, using the GET request on the URL endpoint
	request.open('POST','http://127.0.0.1:5000/storeData/',true);
	request.setRequestHeader('Content-Type', 'application/json');
	
	request.send(JSON.stringify(data));
	request.onload = function() {
	// Begin accessing JSON data here
		var data1 = JSON.parse(this.response)
	}

	// Send request
	//request.send()
	}
} );
	


