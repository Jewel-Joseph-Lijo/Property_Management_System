from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Properties.models import Property
from . models import MaintenanceRequest
from . forms import UpdateMaintanenceRequestForm

# Create your views here.
@login_required
def create_request(request):
    properties=Property.objects.filter(tenant=request.user)
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')   
        property_id = request.POST.get('property')

        MaintenanceRequest.objects.create(
            tenant=request.user,
            property=Property.objects.get(id=property_id),
            title=title,
            description=description
        ) 

        return redirect('Tenant Requests')
    
    return render(request, 'Create_Request.html', {'properties': properties})

@login_required(login_url='login/')
def tenant_requests(request):
    my_requests = MaintenanceRequest.objects .filter(tenant=request.user)
    return render(request, 'Tenant_Requests.html', {'requests': my_requests})

@login_required(login_url='login/')
def all_requests(request):
    allrequests=MaintenanceRequest.objects.all()
    return render(request,'All_Requests.html',{'requests':allrequests})

@login_required(login_url='login/')
def update_request(request,pk):
    request_instance=MaintenanceRequest.objects.get(pk=pk)
    if request.POST:
        form=UpdateMaintanenceRequestForm(request.POST,instance=request_instance)
        if form.is_valid():
            form.save()
        return redirect('All Requests')
    else:
        form=UpdateMaintanenceRequestForm(instance=request_instance)
    return render(request,'Update_Request.html',{'form':form})
    
