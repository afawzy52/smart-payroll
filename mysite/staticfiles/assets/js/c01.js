
var today = new Date();
var hournow = today.getHours();
var greeting;
if (hournow >= 5 && hournow < 12) {
    greeting = "Good Morning";
} else if (hournow >= 12 && hournow < 18) {
    greeting = "Good Afternoon";
} else {
    greeting = "Good Evening";
}
alert(greeting)
document.write('<h3>' + greeting + '</h3>')

var msg = '<h2> browser window</h2><p> width:'+ window.innerWidth +'</p>';
msg += '<p>height:' + window.innerHeight + '</p>';
msg += '<h2>history</h2><p>items:' + window.history.length + '</p>';
msg += '<h2>screen</h2><p>width:' + window.screen.width + '</p>';
msg += '<p>location:' + document.URL + ' </p>';
var el = document.getElementById('info');
el.innerHTML = msg;

document.write(msg);
