from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Certificate
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from core.serializers import CertificateSerializer

class StudentCertificateListAPIView(generics.ListCreateAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        queryset = Certificate.objects.all()
        event_name = self.request.query_params.get('event', None)
        if event_name:
            queryset = queryset.filter(event__name__icontains=event_name)
        return queryset