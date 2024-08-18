from django.contrib import admin

# Register your models here.

from .models import ContractModel

class ContractAdmin (admin.ModelAdmin):
    list_display = ['contract_name', 'start_date', 'end_date', 'salary']

admin.site.register(ContractModel, ContractAdmin)