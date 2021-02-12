from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)

    def __str__(self):
        return self.title

    # def get_comments_count(self):
    #     return Comment.objects.filter(topic__post=self).count()



class Comment(models.Model):
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='どの記事へのコメントか')
    created_at = models.DateTimeField('作成日', default=timezone.now, blank=True)
    good = models.IntegerField('いいね', default=0)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='コメント投稿ユーザID')

    def __str__(self):
        return self.text[:20]

    # def publish_time(self):
    #     publication = timezone.now()
    #     self.save()