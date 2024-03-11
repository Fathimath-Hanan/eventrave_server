

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ParticipantListAPIView(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class CertificateListAPIView(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = CertificateSerializer

class CertificateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = CertificateSerializer

class ScoreListAPIView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class JudgeListAPIView(generics.ListCreateAPIView):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer

class JudgeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
    
class StudentHomeAPIView(APIView):
    def get(self, request):
        # Retrieve all events
        all_events = Event.objects.all()

        # Get the user ID of the logged-in user if authenticated
        user_id = request.user.id if request.user.is_authenticated else None
        
        # Filter participants based on the user ID of the logged-in user if authenticated
        matching_participants = Participant.objects.filter(user_id=user_id) if user_id else []
        
        # Get events registered for the matching participants
        matching_events = Event.objects.filter(participants__in=matching_participants)
        
        # Serialize the events
        all_events_serializer = EventSerializer(all_events, many=True)
        matching_events_serializer = EventSerializer(matching_events, many=True)
        
        # Return the serialized data
        return Response({
            "all_events": all_events_serializer.data,
            "current_std_events": matching_events_serializer.data
        })

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
        all_events_serializer = EventSerializer(all_events, many=True)
        matching_events_serializer = EventSerializer(matching_events, many=True)
        
        # Return the serialized data
        return Response({
            "all_events": all_events_serializer.data,
            "current_judge_events": matching_events_serializer.data
        })

