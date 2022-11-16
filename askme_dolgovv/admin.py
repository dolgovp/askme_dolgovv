from django.contrib import admin
from askme_dolgovv import models

admin.site.register(models.User)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Tag)
admin.site.register(models.QuestionLike)
admin.site.register(models.AnswerLike)
