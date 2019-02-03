import sys
import string

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
}

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())


# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(message):
    messageSeparated = message.split(' ')
    decodeMessage = ''
    for char in messageSeparated:
        if char in inverseMorseAlphabet:
            decodeMessage += inverseMorseAlphabet[char]
        else:
            # CNF = Character not found
            decodeMessage += '<CNF>'
    return decodeMessage



# encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        if char.upper() in morseAlphabet:
            encodedMessage += morseAlphabet[char.upper()] + " "
        else:
            encodedMessage += '<CNF>'
    return encodedMessage