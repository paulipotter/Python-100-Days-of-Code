ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def english_to_morse(message):
    print(f'upper is {message}')

    morse = ""
    for letter in message:
        if ENGLISH_TO_MORSE.get(letter) is not None:
            morse += ENGLISH_TO_MORSE[letter]
        elif letter == ' ':
            morse += ' '
        else:
            morse += letter
    print(morse)


msg = input("what message do you want to encrypt? ").upper()
english_to_morse(msg)
