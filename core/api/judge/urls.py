from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from core.api.judge.judge_home_events import JudgeHomeAPIView



urlpatterns = [
path('homeevents/',JudgeHomeAPIView.as_view()),
]