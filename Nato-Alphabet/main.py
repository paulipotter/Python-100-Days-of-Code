import pandas
# Read csv data into a Dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary that will have the format {"A": "Alpha" ... "Z": "Zulu"
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# Request user input
word = input("Enter a word: ").upper()
phonetic_word = []
# Not list comprehension
# for letter in word:
#     phonetic_word = phonetic_alphabet[letter]

# The list comprehension way
phonetic_word = [phonetic_alphabet[letter] for letter in word]

print(phonetic_word)