
function showTime() {
    const element = document.getElementById("main-area");
    element.innerHTML = '\
    <div class="col-lo-12">\
    <div class=\"card card-body]\"\
    <h1>Reservation for A ROOM</h1>\
    <br>Event Name:<br>\
    <input type="text" name="event_name"><br>\
    Date:<br>\
    <input type="date" name="date"><br>\
    Time begin:<br>\
    <input type="time" name="time_begin"><br>\
    Time end:<br>\
    <input type="time" name="time_end"><br>\
    Number of Attendance:<br>\
    <input type="number" name="Attendance"><br>\
    <input class="btn btn-outline-success my-2 my-sm-0" type="submit" value="Make Reservation">\
    </div>\
    </div>\
    '
    ;
}
