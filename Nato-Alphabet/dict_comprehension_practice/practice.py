# new_dict = { new_key:new_value for item in list }
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# as always, you can add an if statement at the end of either line

import names
from random import randint

# Generate random names
name_list = [names.get_first_name() for i in range(10)]

# Dic comprehension with student list + random numbers as values
students_scores = {student: randint(1, 101) for student in name_list}

# Generate a dict based on the previous one and filter only Key-Value pairs whose value > 59
passed_student = {student: score for (student, score) in students_scores.items() if score > 59}
print(passed_student)

# Take the word of each sentence and calculate the number of letters in each words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(' ')}
print(result)

# Generate dictionary to play with dict comprehension
student_dict = {
    "student": [names.get_first_name() for i in range(4)],
    "score": [randint(1, 101) for i in range(4)]
}
# Convert dictionary to a pandas Dataframe
import pandas

student_data_frame = pandas.DataFrame(student_dict)

# How to iterate through rows of a pandas Dataframe
for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    pass

# Professor Angela's example:
# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}