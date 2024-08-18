from django.contrib import admin

# Register your models here.

from sms_jobs import models

class JobAdmin (admin.ModelAdmin):
    list_display = ['job_title']

admin.site.register(models.JobModel, JobAdmin)