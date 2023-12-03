import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
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
    }

arguments = sys.argv

def main(phrase):
    print(phrase)
    morse_message = []
    for i in phrase:
        i_upper = i.upper()
        if i_upper in NESTED_MORSE:
            morse_message.append(NESTED_MORSE[i_upper])
    morse_message  = ' '.join(morse_message)
    print(morse_message)

try:
    assert len(arguments) == 2 and arguments[1].isalpha(), "the arguments are bad"
    main(arguments[1])

except AssertionError as msg:
    print(msg)