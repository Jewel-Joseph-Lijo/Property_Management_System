from django.shortcuts import render,redirect
from Properties.models import Property
from django.contrib.auth.decorators import login_required
from . models import RentalApplication,MyRentalDetail

# Create your views here.
@login_required(login_url='login/')
def user_property_list(request):
    properties = Property.objects.all()
    return render(request,'User_Property_List.html',{'properties': properties})

@login_required(login_url='login/')
def user_property_detail(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    return render(request,'User_Property_Detail.html',{'properties': ppty_instance})

@login_required(login_url='login/')
def apply_property(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    already_applied = RentalApplication.objects.filter(tenant=request.user, property=ppty_instance).exists()
    if request.POST:
        # create and save the application
        RentalApplication.objects.create(tenant=request.user, property=ppty_instance)
        # redirect to avoid form resubmission on refresh
        return redirect('User Property Detail', pk=pk)
    return render(request, 'Apply_Property.html', {'properties': ppty_instance,'already_applied':already_applied})

@login_required(login_url='login/')
def applications(request):
    user_applications = RentalApplication.objects.filter(application_status='Pending')
    return render(request, 'Applications.html', {'applications': user_applications})

@login_required(login_url='login/')
def my_rentals(request):
    my_applications = RentalApplication.objects.filter(tenant=request.user)
    myn_rentals = MyRentalDetail.objects.filter(tenant=request.user)
    return render(request, 'My_Rentals.html', {'rentals': myn_rentals,'applications': my_applications})

@login_required(login_url='login/')
def my_rental_detail(request):
    user=request.user
    myn_rentals=MyRentalDetail.objects.filter(tenant=request.user,status='Active')
    return render(request,'My_Rental_Detail.html',{'rentals': myn_rentals,'user':user})

@login_required(login_url='login/')
def tenant_info(request, pk):
    ppty_instance = Property.objects.get(pk=pk)
    tenant_detail = MyRentalDetail.objects.get(property=ppty_instance)
    return render(request, 'Tenant_Info.html', {'tenant_detail': tenant_detail, 'property': ppty_instance})

@login_required(login_url='login/')
def approve_application(request, pk):
    application=RentalApplication.objects.get(pk=pk)
    if request.POST:
        application.application_status = 'Approved'
        application.save()

        # Update the property to set it as occupied and assign the tenant
        ppty_instance = application.property
        ppty_instance.is_occupied = True
        ppty_instance.tenant = application.tenant
        ppty_instance.save()

        # Create a MyRentalDetail entry for the tenant
        MyRentalDetail.objects.create(
            tenant=application.tenant,
            property=ppty_instance,
            rent_start_date=request.POST.get('rent_start_date'),
            rent_due_date=request.POST.get('rent_due_date'),
            status='Active'
        )
    return render(request,'Rent_Date.html',{'application':application})

@login_required(login_url='login/')
def reject_application(request, pk):
    application = RentalApplication.objects.get(pk=pk)
    application.application_status = 'Rejected'
    application.save()
    return redirect('Applications')