<html>
<head>
    <title>Final Step</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto+Mono" rel="stylesheet">

    <style>
        h1{
            text-align: center;
            color: #222;
            font-size: 6em;
            margin-top: 3em;
            font-family: 'Roboto Mono', monospace;
        }


    </style>
</head>
<body>
<h1 id="text"></h1>
<script>
    var i = 0;
    var txt = "{{ $decoded }} = {{ $answer }}";
    var speed = 500;

    function typeWriter() {
        if (i < txt.length) {
            document.getElementById("text").innerHTML += txt.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }

    typeWriter();
</script>
</body>
</html>