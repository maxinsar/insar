from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author",verbose_name="Автор")
    message = models.CharField(max_length=400, verbose_name="Сообщение")

    def __str__(self):
        return "Комментарии {0}".format(self.message)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name="Название компании")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    description = models.TextField(max_length=400, verbose_name="Описание компании")
    image = models.ImageField(upload_to='images/posts_images', blank=True, null=True, verbose_name="Логотип компании")
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, blank= True, null=True, verbose_name="Отзывы о компании")
    date_pub = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self):
        return "Пост - {0}".format(self.name)

    def get_absolute_url(self):
        return reverse('get_posts', args=[self.slug])

    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
