<html>
<head>
    <title>QR</title>
</head>
    <body>
        <h1>Scan Code</h1>
        <div id="qrcode"></div>

    </body>
    <script src="js/qr.js"></script>
    <script type="text/javascript">
        new QRCode(document.getElementById("qrcode"), "{{ $message }}");
    </script>
</html>