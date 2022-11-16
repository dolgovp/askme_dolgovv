from django.core.management.base import BaseCommand, CommandError
from askme_dolgovv import models


class Command(BaseCommand):
    help = 'Generates data for models'

    def add_arguments(self, parser):
        parser.add_argument('ratio', nargs='?', action='store')

    def handle(self, *args, **options):
        for i in range(1, int(options['ratio']) + 1):
            nick_str = 'nick' + str(i)
            models.User.objects.bulk_create([
                models.User(id=i, nickname=nick_str)
            ])
        user_id = 1
        for i in range(1, int(options['ratio']) * 10+1):
            models.Question.objects.bulk_create([
                models.Question(user_id=user_id, title="title" + str(i), q_likes_counter=i // 3)
            ])
            if user_id == int(options['ratio']):
                user_id = 1
            else:
                user_id += 1

        return 'ok'
