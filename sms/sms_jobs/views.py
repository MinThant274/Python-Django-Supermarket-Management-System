from django.shortcuts import render

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from sms_jobs import models
from sms_jobs import forms
from django.db.models import Q

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')


class JobListView(LoginRequiredMixin, ListView):
    model = models.JobModel
    context_object_name = 'jobs_list'
    template_name = 'job_list.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "job_title":
                qs = qs.filter(Q(job_title__icontains=sq))

        return qs

class JobCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    form_class = forms.JobCreateForm
    template_name = 'job_create.html'
    login_url = reverse_lazy('login')

class JobDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    context_object_name = "job"
    template_name = 'job_delete.html'
    login_url = reverse_lazy('login')

class JobDetailView(LoginRequiredMixin, DetailView):
    model = models.JobModel
    context_object_name = "job"
    template_name = 'job_detail.html'
    login_url = reverse_lazy('login')

class JobUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy("job_list")
    model = models.JobModel
    form_class = forms.JobUpdateForm
    context_object_name = "job"
    template_name = 'job_update.html'
    login_url = reverse_lazy('login')