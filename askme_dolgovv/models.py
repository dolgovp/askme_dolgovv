QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'answers_number': question_id+1,
        'tags': ['tag' for i in range(question_id//3)]
     } for question_id in range(10)
]