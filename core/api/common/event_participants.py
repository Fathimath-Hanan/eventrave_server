from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers


from core.models import EventRegistration
class EventRegistrationSerializer(serializers.ModelSerializer):
    is_scored = serializers.SerializerMethodField()
    class Meta:
        model = EventRegistration
        fields = [
            'id', 'student', 'event', 'jest_number', 'position','is_scored', 'members', 'created_at', 'updated_at'
        ]

    def get_is_scored(self, obj):
        
        judge = self.context['request'].user
        return obj.judge_scores.filter(judge=judge).exists()
        
class EventParticipantsListAPIView(APIView):
    def get(self, request, event_id):
        participants = EventRegistration.objects.filter(event_id=event_id)
        participants_serializer = EventRegistrationSerializer(participants, many=True,context={'request': request})
        return Response(participants_serializer.data, status=status.HTTP_200_OK)