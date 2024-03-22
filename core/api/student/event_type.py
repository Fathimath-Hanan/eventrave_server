from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event, EventRegistration


class EventTypeAPIView(APIView):
    def get(self, request):
        # Retrieve all events
        all_events = Event.objects.all()

        # Filter group events and individual events
        group_events = all_events.filter(is_group_event=True)
        individual_events = all_events.filter(is_group_event=False)

        # Serialize the events
        group_events_serializer = EventSerializer(group_events, many=True, context={'request': request})
        individual_events_serializer = EventSerializer(individual_events, many=True, context={'request': request})

        # Return the serialized data
        return Response({
            "group_events": group_events_serializer.data,
            "individual_events": individual_events_serializer.data
        })
