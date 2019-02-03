<html>
    <head>
        <title>QR</title>
    </head>
    <body>
        <h1>Submit Code</h1>
        <form action="/qr" method="post">
            @csrf
            <input name="message">
            <input type="submit">
        </form>
    </body>
</html>