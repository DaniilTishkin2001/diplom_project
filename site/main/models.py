
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец статьи", blank=True, null=True)
    title = models.CharField("Название", max_length=50, default="Введите поле название")
    anons = models.CharField("Анонс", max_length=50)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")
    moderation = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"




