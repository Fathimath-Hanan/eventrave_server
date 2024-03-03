
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Participant


class StudentEventRegisterAPIView(APIView):
    def post(self, request,):
        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        event_id = request.data.get('event_id', None)
        
        # Check if the event ID is provided
        if event_id is None:
            return Response({"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the participant object based on the user ID
        participant = Participant.objects.filter(user_id=user_id).first()
        
        if participant is None:
            print("Participant not found")
            participant = Participant.objects.create(user_id=user_id)
            
        # Add the event to the participant's events_registered
        participant.events_registered.add(event_id)
        
        return Response({"message": "Event registered successfully"}, status=status.HTTP_200_OK)