
from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event,EventRegistration
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class StudentHomeAPIView(APIView):
    def get(self, request):
        # Retrieve all events
        all_events = Event.objects.all()

        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        
        registered_events = Event.objects.filter(registrations__student__id=user_id)
        
        
        # Serialize the events
        all_events_serializer = EventSerializer(all_events, many=True, context={'request': request})
        registered_events_serializer = EventSerializer(registered_events, many=True, context={'request': request})
        
        # Return the serialized data
        return Response({
            "all_events": all_events_serializer.data,
            "registered": registered_events_serializer.data
        })
        