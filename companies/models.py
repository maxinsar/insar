from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    message = models.CharField(max_length=400, verbose_name="Сообщение")

    def __str__(self):
        return "Comment {0}".format(self.message)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Vacancy(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название вакансии")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    description = models.TextField(max_length=700, verbose_name="Описание вакансии")
    payments = models.DecimalField(max_digits=19, decimal_places=10, verbose_name="Зарплата")

    def __str__(self):
        return "Вакансия - {0}".format(self.name)

    def get_absolute_url(self):
        return reverse('get_vacancy', args=[self.slug])

    class Meta:
        verbose_name="Вакансия"
        verbose_name_plural="Вакансии"

class Company(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название компании")
    slug = models.SlugField(max_length=30, verbose_name="URL")
    description = models.TextField(max_length=400, verbose_name="Описание компании")
    logo_company = models.ImageField(upload_to='images/logo_comapny', blank=True, null=True, verbose_name="Логотип компании")
    vacancy_company = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Вакансии компании")
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, blank= True, null=True, verbose_name="Отзывы о компании")

    def __str__(self):
        return "Компания - {0}".format(self.name)

    def get_absolute_url(self):
        return reverse('get_company', args=[self.slug])
        
    class Meta:
        verbose_name="Компания"
        verbose_name_plural="Компании"
