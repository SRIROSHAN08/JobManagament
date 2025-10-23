from django.urls import path
from .views import *

urlpatterns=[
    path("",JobView.as_view()),
]