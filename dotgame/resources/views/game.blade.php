<html>
    <head>
        <title>gamey gamey game game</title>
        <style>
            .canvas-container {
                margin: 30px auto;
                display: block;
            }
            p {
                text-align: center;
                color: #333;
            }
        </style>
    </head>
    <body>
        <canvas id="game" width="800" height="600"></canvas>
        <p>give the text to raish</p>
        <input id="hardness" type="range" max="1000" min="5" value="200">
    </body>
    <script>
        const TEXT = "{{ $message }}";
    </script>
    <script src="/js/fabric.js"></script>
    <script src="/js/game.js"></script>
</html>