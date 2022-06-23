from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("expenses/", expenses, name='ex'),
    path("token/", token, name='token'),
    path("new_exp/", ExpCreateView.as_view(), name='new_exp'),
    path("signup/", SignUp.as_view(), name="signup"),
    path('inputTest/', inputTest, name='inputTest')

]

# nonuser
# helloalibek