from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from sms_contracts import models
from sms_contracts import forms

from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')


class ContractListView(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = models.ContractModel
	context_object_name = 'contracts_list'
	template_name = 'contract_list.html'
	
	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "contract_name":
				qs = qs.filter(Q(contract_name__icontains=sq))
			elif search_type == "salary":
				qs = qs.filter(Q(salary__icontains=sq))

		return qs

class ContractCreateView(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contract_list")
	model = models.ContractModel
	form_class = forms.ContractCreateForm
	template_name = 'contract_create.html'

class ContractUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contract_list")
	model = models.ContractModel
	form_class = forms.ContractUpdateForm
	context_object_name = "contract"
	template_name = 'contract_update.html'

class ContractDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contract_list")
	model = models.ContractModel
	context_object_name = "contract"
	template_name = 'contract_delete.html'

class ContractDetailView(LoginRequiredMixin, DetailView):
	login_url = reverse_lazy('login')
	model = models.ContractModel
	context_object_name = "contract"
	template_name = 'contract_detail.html'