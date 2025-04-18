from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_http_methods
from .forms import company_form, branch_form
from .models import company, branch, dept

# Create your views here.

# blank page only
def blank_view(request):
    bra = branch.objects.all().order_by('branch_id')

    context = {"branchs":bra}
    
    return render(request, 'settings/blank.html', context)

def company_blank_view(request):
    return render(request, 'blank_page_company.html')

""" def company_view(request):
    com = get_object_or_404(company, pk=1)
    
    if request.method == 'POST':
        form = company_form(request.POST or None, instance=com)

        if form.is_valid():
            form.save()
            messages.success(request, "Company details updated successfully.")
            return render(request, 'blank_page_company.html', {"form":form})
    else:
        form = company_form(instance=com)

    return render(request, 'blank_page_company.html', {"form":form}) """


# update company data 
def comapny_update_view(request):
    com = get_object_or_404(company, pk=1)
    
    if request.method == 'POST':
        form = company_form(request.POST or None, instance=com)
        if form.is_valid():
            # update the existing `company` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            messages.success(request, "Company details updated successfully.")
            return render(request,'settings/company.html', {"form":form})
    else:
        form = company_form(instance=com)

    return render(request,
                'settings/company.html',
                {"form":form})

                
## Branch --------------------------------------------------------
## Branch list-----
def branch_list_view(request):
    bra = branch.objects.all().order_by('branch_id')

    context = {"branch":bra}
    #context['branch']=bra
    return render(request,
           'settings/branch_list.html', 
          context)

## Branch add new-----


def branch_add_view(request):
    if request.method == 'POST':
        form = branch_form(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
    else:
        context = {'form':branch_form() }
    return render(request, 'settings/branch_add.html', context)
        

## Branch edit-----   
def branch_edit_view(request):
    pass

## Branch delete----- 
@require_http_methods(['DELETE'])
def branch_delete_view(request, pk):
    branch = branch.objects.get(pk=pk)
    branch.delete()
    return HttpResponse('success',status = 204, headers={'HX-Trigger': 'BranchDeleted'})

# modal popup example --------------------------
""" def popup(request):

    if request.method == 'POST':
        id = request.GET.get('id')
        context = {'show': branch.objects.get(id=id)}
        return render(request, 'settings/branch_add.html', context=context)

    context = {'shows': branch.objects.all()}
    return render(request, 'settings/branch_list.html', context=context) """

# Department -----------------------------
## department list -----------------------

def dept_list_view(request):
    department = dept.objects.all().order_by('dept_id')

    context = {"dept":department}
    #context['branch']=bra
    return render(request,
           'settings/department_list.html', 
          context)

