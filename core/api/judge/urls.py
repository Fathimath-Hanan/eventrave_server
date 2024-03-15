from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.api.judge.event_student import EventParticipantListAPIView

from core.api.judge.judge_home import JudgeHomeAPIView
urlpatterns = [
    path('home',JudgeHomeAPIView.as_view()),
    path('event-participants/<int:event_id>/', EventParticipantListAPIView.as_view(), name='event_participants'),
    
]