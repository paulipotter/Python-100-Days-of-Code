import pandas

# Read csv data into a Dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary that will have the format {"A": "Alpha" ... "Z": "Zulu"
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    # Request user input
    word = input("Enter a word: ").upper()

    phonetic_word = []

    # Not list comprehension
    # for letter in word:
    #     phonetic_word = phonetic_alphabet[letter]

    try:
        # The list comprehension way
        phonetic_word = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_phonetic()
    else:
        print(" ".join(phonetic_word))


generate_phonetic()
