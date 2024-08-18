from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from sms_employees import models
from sms_employees import forms
from django.db.models import Q

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')


class EmployeeListView(LoginRequiredMixin, ListView):
    model = models.EmployeeModel
    context_object_name = 'employees_list'
    template_name = 'employee_list.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")
        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "emp_id":
                qs = qs.filter(Q(emp_id__icontains=sq))
            elif search_type == "phone":
                qs = qs.filter(Q(phone__icontains=sq))
            elif search_type == "email":
                qs = qs.filter(Q(email__icontains=sq))
        return qs

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    form_class = forms.EmployeeCreateForm
    template_name = 'employee_create.html'
    login_url = reverse_lazy('login')

class EmployeeUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    form_class = forms.EmployeeUpdateForm
    context_object_name = "employee"
    template_name = 'employee_update.html'
    login_url = reverse_lazy('login')

class EmployeeDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("employee_list")
    model = models.EmployeeModel
    context_object_name = "employee"
    template_name = 'employee_delete.html'
    login_url = reverse_lazy('login')

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = models.EmployeeModel
    context_object_name = "employee"
    template_name = 'employee_detail.html'
    login_url = reverse_lazy('login')