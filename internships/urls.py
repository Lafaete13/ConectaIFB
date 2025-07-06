from django.urls import path
from .views import (InternshipListCreateAPIView, 
                    InternshipRetrieveUpdateDestroyAPIView,
                    ApplicationListCreateAPIView,
                    ApplicationRetrieveUpdateDestroyAPIView
                    )


urlpatterns = [
    path('internships/', InternshipListCreateAPIView.as_view(), name='internship-list-create'),
    path('internships/<int:pk>/', InternshipRetrieveUpdateDestroyAPIView.as_view(), name='internship-retrieve-destroy'),
    path('internships/applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('internships/applications/<int:pk>/', ApplicationRetrieveUpdateDestroyAPIView.as_view(), name='application-retrieve-destroy'),
]