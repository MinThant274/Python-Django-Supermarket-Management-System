from django.db import models

# Create your models here.

from django.utils import timezone
from sms_jobs import models as jm

class ContractModel(models.Model):
    contract_name = models.CharField(max_length=200, verbose_name='Name')
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now())
    end_date = models.DateField(verbose_name='End Date', default=timezone.now())
    description = models.CharField(max_length=300, verbose_name='Description', null=True)
    salary = models.FloatField(verbose_name='Salary', default=0.0)
    job_id = models.ManyToManyField(jm.JobModel)

    def __str__(self):
        return self.contract_name