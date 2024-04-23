from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.api.student.event_register import DeleteRegisteredEvent, StudentEventRegisterAPIView
from core.api.student.event_type import EventTypeAPIView
from core.api.student.home import StudentEventSearchAPIView, StudentHomeAPIView
from core.api.student.student_certificates import StudentCertificateListAPIView



urlpatterns = [
    path('home/',StudentHomeAPIView.as_view()),
    path('event/register/',StudentEventRegisterAPIView.as_view()),
    path('event/register/<int:event_id>/delete/<int:member_id>/',DeleteRegisteredEvent.as_view()),
    path('event/type',EventTypeAPIView.as_view()),
    path('event/list',StudentEventSearchAPIView.as_view()),
    path('certificate/list',StudentCertificateListAPIView.as_view()),
]