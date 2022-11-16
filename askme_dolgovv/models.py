from django.utils.timezone import now
from django.db import models

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'answers_number': question_id + 1,
        'tags': ['tag' + str(i) for i in range(question_id // 3)],
        'likes': abs(question_id - 5)
    } for question_id in range(10)
]


class User(models.Model):
    email = models.EmailField(default='test@gmail.ru')
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default='12345678g')
    avatar = models.ImageField(default='static/img/avatar.jpeg', blank=True)
    registration_data = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.nickname +str(self.id)}'


class TagManager(models.Manager):
    def get_questions_by_tag(self):
        return Question.objects.all().filter(tags__in=self)


class Tag(models.Model):
    tag = models.CharField(max_length=30)
    object = TagManager()


class QuestionManager(models.Manager):
    def get_hot_questions(self):
        return Question.objects.all().order_by('q_likes_counter').reverse()[:50]
    def get_new(self):
        return Question.objects.all().order_by('creation_date').reverse()[:50]


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="title")
    creation_date = models.DateTimeField(default=now)
    q_likes_counter = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    objects = QuestionManager()


class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField


class Answer(models.Model):
    user = models.ForeignKey
    text = models.TextField
    a_likes_counter = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    writing_date = models.DateTimeField(default=now)


class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField
