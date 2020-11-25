from django.urls import path
from .views import *

urlpatterns = [
    path('echo', echoTest.as_view()),
    path('echo-post', echoPostTest.as_view()),
    path('mysql-test', testMySQL.as_view()),
]