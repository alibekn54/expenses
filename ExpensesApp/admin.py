from django.contrib import admin
from .models import *
from .models import Token, Expense
# Register your models here.
admin.site.register(Expense)
admin.site.register(Token)