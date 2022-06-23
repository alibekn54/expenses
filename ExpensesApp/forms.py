from django import forms
from django.forms import Textarea

from .models import Expense


class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Expense
        fields = ['title', 'description', 'money']
        widgets = {
            'name': Textarea(attrs={

            })
        }
