from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from core.api.common.events import EventDetailAPIView, EventListCreateAPIView




urlpatterns = [
    path('events/',EventListCreateAPIView.as_view()),
    path('events/<int:pk>/',EventDetailAPIView.as_view()),
]