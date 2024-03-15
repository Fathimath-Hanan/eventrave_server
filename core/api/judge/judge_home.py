
from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event, Judge
class JudgeHomeAPIView(APIView):
    def get(self, request):
        # Retrieve all events
        all_events = Event.objects.all()

        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        # Filter participants based on the user ID of the logged-in user if authenticated
        matching_judge_events = Judge.objects.filter(user_id=user_id) if user_id else []
        
        # Get events registered for the matching participants
        matching_events = Event.objects.filter(judges__in=matching_judge_events)
        
        # Serialize the events
        all_events_serializer = EventSerializer(all_events, many=True, context={'request': request})
        matching_events_serializer = EventSerializer(matching_events, many=True, context={'request': request})
        
        # Return the serialized data
        return Response({
            "current_judge_events": matching_events_serializer.data
        })