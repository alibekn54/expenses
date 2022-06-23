from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.db.models import Avg, Max, Min, Sum
from .models import Expense,Token
from django.utils.crypto import get_random_string
from django.utils.crypto import get_random_string
from .forms import ExpenseForm


def home(request):
    return render(request, "home.html")


def expenses(request):
    token = Token.objects.all().filter(userId=request.user.id)
    for i in token:
        token2 = i.id

    for t in token:
        tokenUser = i.token

    sum = Expense.objects.all().filter(token=token2).aggregate(Sum('money'))

    all_expenses = Expense.objects.order_by('-pk').filter(token=token2).values()

    TokenInput = request.POST.get('token')
    QuerySetToken = Token.objects.all()
    tokens = []
    for i in QuerySetToken:
        tokens.append(i.token)

    if TokenInput in tokens and TokenInput != tokenUser:
        error_or_suc = 'Success'
    else:
        error_or_suc = 'Error _The written token is not valid OR WRITTEN TOKEN IS YOURS'

    return render(request, "expenses.html", context={'sum': sum, 'all': all_expenses, 'tok': token2, 'iToken': TokenInput, 'errsuc': error_or_suc, 'tokenUser': tokenUser})


def token(request):
    token = Token.objects.all().filter(userId=request.user.id).values()
    unique_id = get_random_string(length=32)
    if not token:
        Token.objects.create(userId=request.user, token=unique_id)
    else:
        return render(request, "token.html", context={'tok': token})

    return render(request, "token.html", context={'tok': token})



def inputTest(request):
    querySet = Expense.objects.order_by().values('title').distinct()
    return render(request, 'testInput.html', {'inputTest': querySet})


class ExpCreateView(CreateView):
    model = Expense
    template_name = 'exp_new.html'
    form_class = ExpenseForm

    def form_valid(self, form):
        form.instance.userId = self.request.user
        token = Token.objects.all().filter(userId=self.request.user.id)
        for i in token:
            token2 = i
        form.instance.token = token2
        return super(ExpCreateView, self).form_valid(form)






    # token = Token.objects.all().filter(userId=request.user.id)
    # for i in token:
    #     token2 = i.id


# class EnterToken(CreateView):
    # мы должны брать тот токен который ввел user и менять полностю его токен на тот токен который ввел;
    # дальше удалять его токен и менять на другой
    # и дальше у нас расходы обьедененены




class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

# qazaqastana007