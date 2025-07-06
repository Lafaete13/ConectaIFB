from django.urls import path
from .views import (EventListCreateAPIView, 
                    EventRetrieveUpdateDestroyAPIView,
                    EventRegistrationListCreateAPIView,
                    EventRegistrationRetrieveUpdateDestroyAPIView
                    )


urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-destroy'),
    path('events/eventsregistration/', EventRegistrationListCreateAPIView.as_view(), name='eventsregistration-list-create'),
    path('events/eventsregistration/<int:pk>/', EventRegistrationRetrieveUpdateDestroyAPIView.as_view(), name='eventsregistration-retrieve-destroy'),
]