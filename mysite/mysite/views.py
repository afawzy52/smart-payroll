from django.shortcuts import render
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2518534075.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1797503747.


# Create your views here.
def index(request):
  
  return render(request,'index.html',{} )