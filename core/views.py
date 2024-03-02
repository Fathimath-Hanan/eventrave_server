from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Participant, Event, Judge, Score
from core.serializers import EventSerializer, ParticipantSerializer, JudgeSerializer, ScoreSerializer, CertificateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class EventListAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name']

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ParticipantListAPIView(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class CertificateListAPIView(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = CertificateSerializer

class ScoreListAPIView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class JudgeListAPIView(generics.ListCreateAPIView):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer

class JudgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
class StudentHomeAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)