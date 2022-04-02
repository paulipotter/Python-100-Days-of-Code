from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(q_text=question['question'], q_answer=question['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"your final score was {quiz.score}/{quiz.question_number}")


# instead, tap into https://opentdb.com/api_config.php to get questions
