from django.db import models
from django.db.models import Sum
from django.utils.crypto import get_random_string

# Create your models here.


class Expense(models.Model):
    userId = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    money = models.FloatField()
    token = models.ForeignKey('Token', on_delete=models.CASCADE)


unique_id = get_random_string(length=32)


class Token(models.Model):
    userId = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.TextField(default=unique_id)




