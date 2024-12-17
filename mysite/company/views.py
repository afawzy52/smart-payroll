from django.shortcuts import render
from django.contrib import messages
from .forms import company_form
from .models import company

# Create your views here.

def comapny_update_view(request):
    com = company.objects.get(pk=1)

    if request.method == 'POST':
        form = company_form(request.POST, instance=com)
        if form.is_valid():
            # update the existing `company` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            messages.success(request, "Company details updated successfully.")
            return redirect('company-update', com.id)
    else:
        form = company_form(instance=com)

    return render(request,
                'settings/company.html',
                {'form': form})







