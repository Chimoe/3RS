function showHome(){
    var element = document.getElementById("main-area");
    element.innerHTML = '\n' +
        '<h3>Buildings Available for Reservation</h3>\n' +
        '{% if buildings %}\n' +
        '<ul>\n' +
        '    {% for building in buildings %}\n' +
        '    <li><a href="#" onclick="showBuliding()">{{building.name}}</a></li>\n' +
        '    {% endfor %}\n' +
        '</ul>\n' +
        '{% else %}\n' +
        '<h3>No Buildings Are Available</h3>\n' +
        '    {% endif %}';
}

function showBuliding(){
    var element = document.getElementById("main-area");
    element.innerHTML = '\
				<div class="discover">\
					<div class="row">\
						<div class="col-lg-6">\
							<h3>DCC</h3>\
							<p>608<br/>702<br/>114<br/>514<br/>810</p>\
						</div>\
						<div class="col-lg-6">\
							<h3>Low</h3>\
							<p></p>\
						</div>\
						<div class="col-lg-6">\
							<h3>Lally</h3>\
							<p></p>\
						</div>\
						<div class="col-lg-6">\
							<h3>Whatever</h3>\
							<p></p>\
						</div>\
					</div>\
				</div>\
		<br><br><p><a href="#" onclick="showHome()">Home</a></p>\
		<br\><br\><p><a href="https://webforms.rpi.edu/special-event-room-reservation-requests" class="Form">Form url</a></p>'
    ;
}
