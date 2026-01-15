from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Properties.models import Property
from Tenants.models import MyRentalDetail
from Accounts.models import User
from . models import Payment
from datetime import timedelta
from random import randrange

# Create your views here.
@login_required(login_url='login/')
def payment_summary(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    rental_detail = MyRentalDetail.objects.filter(property=ppty_instance,status='Active')
    for detail in rental_detail:
        rent_due_date = detail.rent_due_date
    return render(request, 'Payment_summary.html',{'property': ppty_instance,'rent_due_date':rent_due_date})

@login_required(login_url='login/')
def payment_form(request,pk):
    ppty_instance=Property.objects.get(pk=pk)
    rent_amount = ppty_instance.rent_amount
    return render(request, 'Payment_Form.html',{'rent_amount': rent_amount,'property': ppty_instance})

@login_required(login_url='login/')
def payment_success(request,pk):
    if request.GET:
        ppty_instance = Property.objects.get(pk=pk)
        payment_method = request.POST.get('payment_method') or request.GET.get('payment_method')

        payment = Payment.objects.create(
            tenant=request.user,
            property=ppty_instance,
            amount=ppty_instance.rent_amount,
            payment_method=payment_method,
            status="Success",
            transaction_id=f"TXN{request.user.id}{ppty_instance.id}{randrange(10000,99999)}"
        )

        rental_detail = MyRentalDetail.objects.filter(property=ppty_instance, status='Active')
        for detail in rental_detail:
            rent_start_date = detail.rent_due_date
            rent_due_date = detail.rent_due_date + timedelta(days=30)
        rental_detail.update(rent_start_date=rent_start_date, rent_due_date=rent_due_date)

    return render(request, 'Payment_Reciept.html', {'payment_info': payment})

@login_required(login_url='login/')
def payment_history(request):
    payments = Payment.objects.filter(tenant=request.user).order_by('payment_date')
    return render(request, 'Payment_History.html', {'payments': payments})

@login_required(login_url='login/')
def all_payment_history(request):
    payments=Payment.objects.all()
    tenants=User.objects.all()
    properties=Property.objects.all()
    return render(request, 'All_Payment_History.html', {'payments': payments,'tenants': tenants,'properties':properties})