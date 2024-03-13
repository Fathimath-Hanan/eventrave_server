from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('core.api.common.urls')),
    path('student/', include('core.api.student.urls')),
    path('judge/', include('core.api.judge.urls')),
]