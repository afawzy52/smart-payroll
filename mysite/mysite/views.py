from django.shortcuts import render
from django.contrib.auth.models import User
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2518534075.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1797503747.


# Create your views here.
def base_page_view(request):
  user= User.objects.get(pk=1)
  context={'user':user}
  return render(request,'base.html',{'context':context})

def index(request):
  
  return render(request,'index.html',{} )

def login(request):
  
  return render(request,'login.html',{} )

def register(request):
  
  return render(request,'register.html',{} )

