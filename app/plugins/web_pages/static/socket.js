var timerID = 0;

var socket;
let socket_url = "ws://" + document.domain + ':' + '5001'

function start() {
    socket = new WebSocket(socket_url);
    socket.onopen = function (event) {
        if (window.timerID) {
            window.clearInterval(window.timerID);
            window.timerID = 0;
        }
    }

    socket.onclose = function (event) {
        if (!window.timerID) {
            window.timerID = setInterval(function () { start(socket_url) }, 5000);
        }
    }

    socket.onmessage = function (event) {
        message = JSON.parse(event.data)
        if (message.command == 'rename') {
            $('#btn' + message.number).html(message.name)
        }
    }
}

// register every button to send messages
$(function () {
    $('button').bind('click', function () {
        var msg = { 'command': 'click', 'button': 0 }
        msg.button = this.value
        socket.send(JSON.stringify(msg))
    });
    // $('button').bind('mousedown', function() {
    //     socket.send('down:' + this.value)
    // });
    // $('button').bind('mouseup', function() {
    //     socket.send('up:' + this.value)
    // });
});