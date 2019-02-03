
<html>
<head>
    <title>STEP 1 | Quackathon</title>
</head>
<body>
<h1>Decrypt message</h1>
<form method="post" action="/game">
    @csrf
    <input name="message">
    <input type="submit">
</form>
</body>
</html>
