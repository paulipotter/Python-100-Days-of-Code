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


def encrypt(message):
    print(f'upper is {message}')

    morse = []
    for letter in message:
        if ENGLISH_TO_MORSE.get(letter) is not None:
            morse += ENGLISH_TO_MORSE[letter]
        elif letter == ' ':
            pass
        else:
            morse += letter
    return ' '.join(morse)


def decrypt(message):
    message = message.split(' ')
    plain_text = []
    for code in message:
        if code in morse_to_english_dict:
            plain_text += morse_to_english_dict[code]
    print(plain_text)
    return ' '.join(plain_text)


morse_to_english_dict = {}
for key, value in ENGLISH_TO_MORSE.items():
    morse_to_english_dict[value] = key
msg = input("what message do you want to encrypt? ").upper()
# encrypt(msg)
print(decrypt(msg))