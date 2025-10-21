from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('signup', signup_view, name="signup"),
    path('login', login_view, name="login"),
]
