# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.event_participants import EventRegistrationSerializer
from core.models import EventRegistration


class RegisteredParticipantsAPIView(APIView):
    def get(self, request, event_id):
        try:
            event_registrations = EventRegistration.objects.filter(event__id=event_id)
            serializer = EventRegistrationSerializer(event_registrations, many=True)
            return Response(serializer.data)
        except EventRegistration.DoesNotExist:
            return Response({"message": "Event not found"}, status=404)
