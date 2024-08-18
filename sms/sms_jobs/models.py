from django.db import models

# Create your models here.

class JobModel(models.Model):
    job_title = models.CharField(max_length=200, verbose_name='job_title')
    expected_employees = models.IntegerField(verbose_name='Expected Employees', default=0)
    
    def __str__(self):
        return self.job_title