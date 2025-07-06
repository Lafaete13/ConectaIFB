from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Internship, Application
from .serializers import InternshipSerializer, ApplicationSerializer


class InternshipListCreateAPIView(ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class InternshipRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer


class ApplicationListCreateAPIView(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer