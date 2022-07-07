english_to_morse_dict = {'A': '.-', 'B': '-...',
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
morse_to_english_dict = {}


def encrypt(message):
    morse = []
    for letter in message:
        if english_to_morse_dict.get(letter) is not None:
            morse.append(english_to_morse_dict[letter])
    return ' '.join(morse)


def decrypt(message):
    message = message.split(' ')
    plain_text = []
    for code in message:
        if code in morse_to_english_dict:
            plain_text += morse_to_english_dict[code]
    print(plain_text)
    return ' '.join(plain_text)


def main():
    # make morse to english dict from the existing dict
    print('***morse code converter***')
    while True:
        command = ''
        msg = input("\nPlease type your message: ").upper()

        while command != 'E' and command != 'D':
            command = input("""Please type E to encrypt or D to decrypt: """).upper()
            if command == 'E':
                text = encrypt(msg)
                print(f'Encrypted message: {text}')
            elif command == 'D':
                text = decrypt(msg)
                print(f'Decrypted message: {text}')
            else:
                print('Option not valid, please try again.\n')
        print('\nprogram will restart...\n')


if __name__ == "__main__":
    for key, value in english_to_morse_dict.items():
        morse_to_english_dict[value] = key
    main()
