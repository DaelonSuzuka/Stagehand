web_template = """
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>


<script type=text/javascript>
    var timerID=0;

    var socket;
    let socket_url = "ws://" + document.domain + ':' + '5001'
    

    function start(){
        socket = new WebSocket(socket_url);
        socket.onopen = function(event) {
            if(window.timerID) {
                window.clearInterval(window.timerID);
                window.timerID=0;
            }
        }
           
        socket.onclose=function(event){
            if (!window.timerID) {
                window.timerID = setInterval(function(){start(socket_url)}, 5000);
            }
        }

        socket.onmessage = function (event) {
            message = JSON.parse(event.data)
            if (message.command == 'rename') {
                $('#btn'+message.number).html(message.name)
            }
        }
    }
    
    start();

    // register every button to send messages
    $(function() {
        $('button').bind('click', function() {
            socket.send(this.value)
        });
        // $('button').bind('mousedown', function() {
        //     socket.send('down:' + this.value)
        // });
        // $('button').bind('mouseup', function() {
        //     socket.send('up:' + this.value)
        // });
    });
</script>


<html>

<body style="background-color: #1F1E1F; color:white;">
    <style>
        canvas {
            background-color: #1F1E1F;
            overflow-y: auto;
        }

        @media (min-width: 600px) {
            button {
                font-family: Helvetica;
                background-color: #3A393A;
                color: white;
                height: 250px;
                width: 250px;
                font-size:30px;
            }
        }

        @media (max-width: 600px) {
            button {
                font-family: Helvetica;
                background-color: #3A393A;
                color: white;
                width: 150px;
                height: 150px;
                font-size: 20px;
            }
        }
    </style>

    <div class='canvas'>
        <button id='btn1' value="1">1</button>
        <button id='btn2' value="2">2</button>
        <button id='btn3' value="3">3</button>
        <button id='btn4' value="4">4</button>
        <button id='btn5' value="5">5</button>
        <button id='btn6' value="6">6</button>
        <button id='btn7' value="7">7</button>
        <button id='btn8' value="8">8</button>
        <button id='btn9' value="9">9</button>
        <button id='btn10' value="10">10</button>
        <button id='btn11' value="11">11</button>
        <button id='btn12' value="12">12</button>
    </div>
    <div class="message_holder"></div>
</body>

</html>
"""