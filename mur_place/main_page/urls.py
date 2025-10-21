from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('auth', auth_view),
    path('reg', reg_view),
]
