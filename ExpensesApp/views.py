from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.db.models import Avg, Max, Min, Sum
from .models import Expense,Token
from django.utils.crypto import get_random_string

# Create your views here.


def home(request):
    return render(request, "home.html")


def expenses(request):
    sum = Expense.objects.all().filter(userId=request.user.id).aggregate(Sum('money'))
    token = Token.objects.all().filter(userId=request.user.id)
    return render(request, "expenses.html", context={'sum': sum, 'token': token})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

