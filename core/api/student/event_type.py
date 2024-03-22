from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event, EventRegistration


class EventTypeAPIView(APIView):
    def get(self, request):
        # Retrieve all events
        all_events = Event.objects.all()

        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        # Filter group events and individual events
        group_events = all_events.filter(is_group_event=True)
        individual_events = all_events.filter(is_group_event=False)
        
        # Filter registered group events and individual events for the user
        registered_group_events = group_events.filter(registrations__student__id=user_id)
        registered_individual_events = individual_events.filter(registrations__student__id=user_id)

        # Serialize the events
        all_events_serializer = EventSerializer(all_events, many=True, context={'request': request})
        registered_group_events_serializer = EventSerializer(registered_group_events, many=True, context={'request': request})
        registered_individual_events_serializer = EventSerializer(registered_individual_events, many=True, context={'request': request})
        
        # Return the serialized data
        return Response({
            "group_events": all_events_serializer.data,
            "individual_events": registered_individual_events_serializer.data,
            "registered_group_events": registered_group_events_serializer.data
        })
