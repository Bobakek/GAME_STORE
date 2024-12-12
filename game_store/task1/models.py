from django.db import models

# Create your models here.
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Имя покупателя (username)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение возраста 18+
    buyers = models.ManyToManyField(Buyer, related_name="games")  # Покупатели

    def __str__(self):
        return self.title
class News(models.Model):
    title = models.CharField(max_length=200)  # Заголовок новости
    content = models.TextField()              # Содержимое новости
    date = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.title