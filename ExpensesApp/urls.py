from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("expenses/", expenses, name='ex'),
    path("signup/", SignUp.as_view(), name="signup"),

]

# nonuser
# helloalibek