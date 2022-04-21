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



