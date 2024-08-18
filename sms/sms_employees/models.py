from django.db import models

# Create your models here.

from django.utils import timezone
from sms_contracts import models as cm

class EmployeeModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    birthday = models.DateField(verbose_name='Birthday', default=timezone.now())
    emp_id = models.CharField(max_length=200, verbose_name='Employee ID', null=True)
    email = models.CharField(max_length=200, verbose_name='Email', null=True)
    address = models.CharField(max_length=200, verbose_name='Address')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')
    image = models.ImageField(upload_to='imgs/', default=None, null=True, blank=True)
    contract_id = models.ForeignKey(cm.ContractModel, on_delete=models.CASCADE, default=None, null=True, blank=True)