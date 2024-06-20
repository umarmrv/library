from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.IntegerField()
    isbn = models.IntegerField()
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
