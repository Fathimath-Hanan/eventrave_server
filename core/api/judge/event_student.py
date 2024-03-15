from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Event, Participant
from core.serializers import ParticipantSerializer

class EventParticipantListAPIView(APIView):
    def get(self, request, event_id):
        try:
            # Retrieve the event object
            event = Event.objects.get(pk=event_id)
            
            # Retrieve participants for the event
            participants = event.participants.all()
            
            # Serialize the participants
            participant_serializer = ParticipantSerializer(participants, many=True)
            
            # Return the serialized data
            return Response(participant_serializer.data)
        except Event.DoesNotExist:
            # Handle the case where the event does not exist
            return Response({"detail": "Event not found."}, status=404)
