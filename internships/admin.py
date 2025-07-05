from django.contrib import admin
from internships.models import Internship, Application

admin.site.register([Internship, Application])