from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from core.api.student.event_register import StudentEventRegisterAPIView
from core.api.student.event_type import EventTypeAPIView
from core.api.student.home import StudentHomeAPIView


urlpatterns = [
    path('home/',StudentHomeAPIView.as_view()),
    path('event/register/',StudentEventRegisterAPIView.as_view()),
    path('event/type',EventTypeAPIView.as_view()),
]