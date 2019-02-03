import base64
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

server.starttls()

#Next, log in to the server
server.login("hashdevauto@gmail.com", "Miguel2000")

def to_morse_code(text):
    code = {' ': '|', 'a': '. ', 'b': ' . . .', 'c': '_ . _ .', 'd': '_ . .', 'e': '.', 'f': '. . _ .',
            'g': '_ .', 'h': '. . . .', 'i': '. .', 'j': '. _ _ _', 'k': ' . ', 'l': '. _ . .', 'm': ' _',
            'n': '_ .', 'o': '_ _ ', 'p': '. _ _ .', 'q': ' _ . ', 'r': '. _ .', 's': '. . .', 't': '',
            'u': '. . ', 'v': '. . . _', 'w': '. _ _', 'x': ' . . ', 'y': ' . _ ', 'z': ' _ . .',
            '1': '. _ _ _ _', '2': '. . _ _ _', '3': '. . . _ _', '4': '. . . . _', '5': '. . . . .',
            '6': '_ . . . .', '7': '_ _ . . .', '8': '_ _ _ . .', '9': '_ _ _ _ .', '0': '_ _ _ _ _'}
    morse_code = ""

    for x in text:
        morse_code += code[x.lower()]

    return morse_code

buffer = open("demofile.txt", "r")
text64 = buffer.read()

# print(to_morse_code(text))
text64 += "=" * ((4 - len(text64) % 4) % 4)
text64 = base64.standard_b64decode(text64).decode("utf-8")
# print

rot13 = text64.upper()
key = 13
decryp_text = ""

for i in range(len(rot13)):
    temp = ord(rot13[i]) - key
    if ord(rot13[i]) == 32:
        decryp_text += " "
    elif temp < 65:
        temp += 26
        decryp_text += chr(temp)
    else:
        decryp_text += chr(temp)
msg = """From: hashdevauto@gmail.com
To: myonchev99@gmail.com\n
Subject: <Quackaton message>\n
Hello!\Your morse code message here :
""" + to_morse_code(decryp_text)

# print("The Decrypted message is ", decryp_text)
morse = ("The morse code is: %s ",to_morse_code(decryp_text))
#server.sendmail['Subject'] = "SUBJECT OF THE MAIL"

server.sendmail("hashdevauto@gmail.com", "myonchev99@gmail.com", msg)
server.sendmail("hashdevauto@gmail.com", "ovidiu.andrey97@gmail.com", msg)
# print("In Morse Code", to_morse_code(decryp_text))
