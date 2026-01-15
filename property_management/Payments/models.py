from django.db import models
from django.conf import settings
from Properties.models import Property

# Create your models here.
class Payment(models.Model):
    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Success", "Success"),
        ("Failed", "Failed"),
    ]

    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments")
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50,null=True,blank=True)

    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="Pending")
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateField(auto_now_add=True)
    payment_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant} - ₹{self.amount} ({self.status})"