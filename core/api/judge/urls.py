from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from core.api.judge.judge_home import JudgeHomeAPIView
urlpatterns = [
    path('home',JudgeHomeAPIView.as_view()),
    
]