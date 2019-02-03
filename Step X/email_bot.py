import smtplib, getpass

password =  getpass.getpass("Please Input the password: ")
string = raw_input("Please Input string: ")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.starttls()

#Next, log in to the server
server.login("hashdevauto@gmail.com", password)

#Send the mail
msg = string # The /n separates the message from the headers
server.sendmail("hashdevauto@gmail.com", "barrow.jacob@gmail.com", msg)
