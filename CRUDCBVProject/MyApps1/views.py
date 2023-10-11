#DetailView
from django.shortcuts import render
from MyApps1.models import Company
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
class CompanyCreateView(CreateView):
    model=Company
    fields = ('name', 'location', 'ceo')
class CompanyListView(ListView):
    model=Company
    #default template_name is company_list.html
    #defult context_object_name is company_list var
class CompanyDetailView(DetailView):
    model=Company
    #default template_name is company_detail.html
    #defult context_object_name is company or given-object for company_list in usage in company_list.html


from django.views.generic import UpdateView
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name','ceo');

from django.views.generic import DetailView
from django.urls import reverse_lazy
class CompanyDeleteView(DetailView):
    model = Company
    success_url=reverse_lazy('Companies')
