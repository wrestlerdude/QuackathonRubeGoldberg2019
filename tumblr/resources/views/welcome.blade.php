<html>
    <head>
        <title>STEP 1 | Quackathon</title>
    </head>
    <body>
        <h1>Send a message</h1>
        <form method="post" action="/submit">
            @csrf
            <input name="message">
            <input type="submit">
        </form>
    </body>
</html>
