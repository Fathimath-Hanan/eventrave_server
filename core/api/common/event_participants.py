from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers


from core.models import EventRegistration
class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = "__all__"
        
class EventParticipantsListAPIView(APIView):
    def get(self, request, event_id):
        participants = EventRegistration.objects.filter(event_id=event_id)
        participants_serializer = EventRegistrationSerializer(participants, many=True)
        return Response(participants_serializer.data, status=status.HTTP_200_OK)