from .models import Quiz
def quiz_json(quiz:Quiz):
    return {
        'id': quiz.id,
        'question': quiz.question,
        'options': quiz.options,
        'right_answer': quiz.right_answer,
        'status': quiz.status,
        'start_date': quiz.start_date,
        'end_date': quiz.end_date
    }
    