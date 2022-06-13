from django.db import models
from django.utils.crypto import get_random_string
from django.db.models import Sum

unique_id = get_random_string(length=15)
# Create your models here.


class Expense(models.Model):
    userId = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    token = unique_id
    sum = Expense.objects.aggregate(Sum('price'))


