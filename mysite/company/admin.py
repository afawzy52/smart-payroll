from django.contrib import admin
from .models import company,dept, branch, job_title

# Register your models here.
admin.site.register([company,dept,branch,job_title])
