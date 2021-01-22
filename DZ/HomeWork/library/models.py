from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    name = models.CharField('Название поставщика ' ,max_length=50)
    field = models.CharField('Поставляемый продукт ' ,max_length=500)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField('Название библиотеки' ,max_length=50)
    number = models.CharField('Контактный номер' ,max_length=50, default=1)
    Post = models.ManyToManyField(Post, blank=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    name = models.CharField('Название книги',max_length=50)
    quantity = models.IntegerField('Количество' ,max_length=1000)
    author = models.CharField('Автор' ,max_length=50)
    description = models.CharField('Описание' ,max_length=1000)
    def __str__(self):
        return self.name



