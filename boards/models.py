from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='どの記事へのコメントか')

    def __str__(self):
        return self.text[:20]