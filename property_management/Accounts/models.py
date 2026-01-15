from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLES=(
        ('admin','Admin'),
        ('company_admin','Company Admin'),
        ('tenant','Tenant')
    )

    full_name=models.CharField(max_length=20,blank=False,null=False,default='Unknown')
    role=models.CharField(max_length=20,choices=USER_ROLES,default='tenant')
    ph_no=models.CharField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.full_name

