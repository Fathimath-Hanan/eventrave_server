from rest_framework import serializers
from account.views import CustomUserSerializer

from core.models import EventJudges, Judge, Participant, Event, Certificate, Score



class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class JudgeSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email')
    user_first_name = serializers.CharField(source='user.first_name')
    user_last_name = serializers.CharField(source='user.last_name')
    user_branch = serializers.CharField(source='user.branch')
    assigned_events_names = serializers.SerializerMethodField()

    class Meta:
        model = Judge
        fields = ['id', 'user_email', 'user_first_name', 'user_last_name', 'user_branch', 'assigned_events_names']

    def get_assigned_events_names(self, obj):
        assigned_events = obj.assigned_events.all()
        return [event.name for event in assigned_events]


class ScoreSerializer(serializers.ModelSerializer):
    event_name = serializers.SerializerMethodField()
    participant_name = serializers.SerializerMethodField()
    judge_name = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ['id', 'score', 'remarks', 'event', 'participant', 'judge', 'event_name', 'participant_name', 'judge_name']

    def get_event_name(self, obj):
        return obj.event.name if obj.event else None

    def get_participant_name(self, obj):
        return obj.participant.user.username if obj.participant else None

    def get_judge_name(self, obj):
        return obj.judge.user.username if obj.judge else None


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

