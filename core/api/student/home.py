from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event, EventRegistration
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class StudentHomeAPIView(APIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name']
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        # Apply filters directly to the queryset
        queryset = self.queryset

        # Apply search filter if 'search' parameter is provided in the request
        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        # Filter registered events for the logged-in user
        registered_events = Event.objects.filter(registrations__student__id=user_id)

        # Serialize the events
        all_events_serializer = self.serializer_class(queryset, many=True, context={'request': request})
        registered_events_serializer = EventSerializer(registered_events, many=True, context={'request': request})

        # Return the serialized data
        return Response({
            "all_events": all_events_serializer.data,
            "registered": registered_events_serializer.data
        })
