from django.db import models
from django.conf import settings

# Create your models here.
class Property(models.Model):
    PROPERTY_TYPES = [
        ('House', 'House'),
        ('Office', 'Office Space'),
        ('Shop', 'Shop'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default='House')
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    is_occupied = models.BooleanField(default=False)
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rented_properties'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.property_type})"