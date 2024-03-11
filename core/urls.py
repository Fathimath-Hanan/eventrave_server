from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from core.views import CertificateDetailAPIView, CertificateListAPIView, EventDetailAPIView, EventListAPIView, JudgeDetailAPIView, JudgeHomeAPIView, JudgeListAPIView, ParticipantDetailAPIView, ParticipantListAPIView, ScoreDetailAPIView, ScoreListAPIView, StudentHomeAPIView

urlpatterns = [
    path('event/',EventListAPIView.as_view()),
    path('event/<int:pk>/',EventDetailAPIView.as_view()),
    path('participant/',ParticipantListAPIView.as_view()),
    path('participant/<int:pk>/',ParticipantDetailAPIView.as_view()),
    path('certificate/',CertificateListAPIView.as_view()),
    path('certificate/<int:pk>/',CertificateDetailAPIView.as_view()),
    path('score/',ScoreListAPIView.as_view()),
    path('score/<int:pk>/',ScoreDetailAPIView.as_view()),
    path('judge/',JudgeListAPIView.as_view()),
    path('judge/<int:pk>/',JudgeDetailAPIView.as_view()),
    path('studenthome/',StudentHomeAPIView.as_view()),
    path('judgehome/',JudgeHomeAPIView.as_view())
]
urlpatterns = [
    path('', include('core.api.common.urls')),
    path('student/', include('core.api.student.urls')),
   
]