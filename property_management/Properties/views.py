from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Property
from . forms import PropertyForm
from Accounts.models import User
from Tenants.models import RentalApplication
from Maintenance.models import MaintenanceRequest
from Payments.models import Payment
from django.db.models import Sum


# Create your views here.
@login_required(login_url='login/')
def company_home(request):
    property_count=Property.objects.all().count()
    apply_count=RentalApplication.objects.filter(application_status='Pending').count()
    maintenance_count=MaintenanceRequest.objects.all().count()
    rent_amount_sum=Payment.objects.aggregate(Sum('amount'))['amount__sum']
    last_payment=Payment.objects.last()
    last_property=Property.objects.last()
    last_application=RentalApplication.objects.filter(application_status='Pending').last()
    last_maintenance=MaintenanceRequest.objects.filter(status='Pending').last()
    counts={
        'property_count':property_count,
        'apply_count':apply_count,
        'maintenance_count':maintenance_count,
        'rent_amount_sum':rent_amount_sum,
        'last_payment':last_payment,
        'last_property':last_property,
        'last_application':last_application,
        'last_maintenance':last_maintenance
    }
    return render(request,'Company_Home.html',counts)

@login_required(login_url='login/')
def add_property(request):
    if request.POST:
        form=PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Add Property')
    else:
       form=PropertyForm()
    return render(request,'Add_Property.html',{'form':form})

@login_required(login_url='login/')
def property_list(request):
    properties = Property.objects.all()
    return render(request,'Property_List.html',{'properties': properties})

@login_required(login_url='login/')
def property_detail(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    return render(request,'Property_Detail.html',{'properties': ppty_instance})

@login_required(login_url='login/')
def edit_property(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    if request.POST:
        form=PropertyForm(request.POST,request.FILES,instance=ppty_instance)
        if form.is_valid():
            form.save()
        return redirect('Property List')
    else:
       form=PropertyForm(instance=ppty_instance) 
       form.fields['tenant'].queryset = User.objects.filter(role='tenant')
    return render(request,'Edit_Property.html',{'form':form})

@login_required(login_url='login/')
def delete_property(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    ppty_instance.delete()
    properties = Property.objects.all()
    return render(request,'Property_List.html',{'properties': properties})
