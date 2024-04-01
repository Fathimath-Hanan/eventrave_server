
from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event,EventRegistration
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class StudentHomeAPIView(APIView):

    def get(self, request):
        all_events = Event.objects.all()
        user_id = request.user.id if request.user.is_authenticated else None
        registered_events = Event.objects.filter(registrations__student__id=user_id)
        
        all_events_serializer = EventSerializer(all_events, many=True, context={'request': request})
        registered_events_serializer = EventSerializer(registered_events, many=True, context={'request': request})
        return Response({
            "all_events": all_events_serializer.data,
            "registered": registered_events_serializer.data
        })
    
class StudentEventSearchAPIView(generics.ListCreateAPIView):
    filter_backends=(DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields = ['name']
    queryset = Event.objects.all()
    serializer_class = EventSerializer
