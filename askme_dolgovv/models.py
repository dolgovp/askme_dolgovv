QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'answers_number': question_id+1,
        'tags': ['tag'+str(i) for i in range(question_id//3)],
        'likes':abs(question_id-5)
     } for question_id in range(10)
]