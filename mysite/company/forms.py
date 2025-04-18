# Suggested code may be subject to a license. Learn more: ~LicenseLog:1873772402.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:676380680.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import company, dept, branch, job_title


#user = User.objects.get(pk=1)

class company_form(forms.ModelForm):
   class Meta:
     model = company
     exclude = ["com_id","com_slug","created_at"]

class branch_form(forms.ModelForm):
   class Meta:
     model = branch
     fields = "__all__" 
     

class dept_form(forms.ModelForm):
   class Meta:
     model = dept
     fields = "__all__"
     

    

