from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Certificate
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from core.serializers import CertificateSerializer

class StudentCertificateListAPIView(generics.ListCreateAPIView):
    serializer_class = CertificateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['event__name']  # Specify the field you want to search against

    def get_queryset(self):
        return Certificate.objects.all()