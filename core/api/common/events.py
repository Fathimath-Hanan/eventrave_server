from rest_framework import serializers,generics
from core.models import Event
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
        
class EventListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name']

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer