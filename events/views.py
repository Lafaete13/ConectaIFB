from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer


class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRegistrationListCreateAPIView(ListCreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

class EventRegistrationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer