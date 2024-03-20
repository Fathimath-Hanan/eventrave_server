
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import EventRegistration


class StudentEventRegisterAPIView(APIView):
    def post(self, request,):
        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        event_id = request.data.get('event_id', None)
        members = request.data.get('members', [])
        # Check if the event ID is provided
        if event_id is None:
            return Response({"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the participant object based on the user ID
        participant = EventRegistration.objects.filter(event_id=event_id, student_id=user_id).first()
        
        if participant is None:
            print("Participant not found")
            participant = EventRegistration.objects.create(event_id=event_id, student_id=user_id)
            participant.members.set(members)
            participant.save()
            

        
        return Response({"message": "Event registered successfully"}, status=status.HTTP_200_OK)