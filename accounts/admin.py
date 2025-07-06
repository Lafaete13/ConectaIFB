from django.contrib import admin
from accounts.models import StudentProfile, AdminProfile, CompanyProfile


admin.site.register([StudentProfile, AdminProfile, CompanyProfile])
