from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.common.events import EventSerializer
from core.models import Event


class JudgeHomeAPIView(APIView):
    def get(self, request):
        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        # Retrieve events assigned to the current judge
        judge_events = Event.objects.filter(judges__id=user_id)
        
        # Serialize the judge events
        judge_events_serializer = EventSerializer(judge_events, many=True, context={'request': request})
        
        # Return the serialized data
        return Response({
            "judge_events": judge_events_serializer.data,
        })
