from django.db import models
from django.conf import settings
from Properties.models import Property

# Create your models here.
class MyRentalDetail(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'})
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    rent_start_date = models.DateField()
    rent_due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Active', 'Active'),
        ('Completed', 'Completed')
    ], default='Active')

    def __str__(self):
        return f"{self.tenant.full_name} - {self.property.name if self.property else 'No Property'}"


class RentalApplication(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'tenant'})
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ], default='Pending')
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant.full_name} - {self.property.name} ({self.application_status})"