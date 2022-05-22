from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_public = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default=" ", verbose_name='Текст статьи')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
