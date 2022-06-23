from django.contrib import admin
from .models import *
from .models import Token, Expense
# Register your models here.
admin.site.register(Expense)
admin.site.register(Token)


'''
1) создать кнопку __ввести токен CreateView__  done
2) Переделать QuerySet в expenses чтобы записи доставал не по айди а по токену done
3) Создать возможность генерировать новый токен (Предупреждать user потеряет все данные)
3.1) Удалять старый токен
 
'''