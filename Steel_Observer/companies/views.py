from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.companies.forms import CompanyCreateForm, CompanyEditForm, CompanyDeleteForm
from Steel_Observer.companies.models import Company


def user_created_company(self):
    company = get_object_or_404(Company, user=self.request.user)
    return self.request.user == company.user


class CompanyCreateView(LoginRequiredMixin, CreateView):

    model = Company
    form_class = CompanyCreateForm
    template_name = 'companies/company-create.html'

    def form_valid(self, form):

        company = form.save(commit=False)
        company.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        company.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company-list')


class CompanyDetailsView(DetailView):

    model = Company
    template_name = 'companies/company-details.html'

    def user_created_company(self):
        company = get_object_or_404(Company, user=self.request.user)
        return self.request.user == company.user


class CompanyEditView(LoginRequiredMixin, UpdateView):

    model = Company
    form_class = CompanyEditForm
    template_name = 'companies/company-edit.html'

    def user_created_company(self):
        company = get_object_or_404(Company, user=self.request.user)
        return self.request.user == company.user

    def form_valid(self, form):

        company = form.save(commit=False)
        company.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        company.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company-list')


class CompanyDeleteView(LoginRequiredMixin, DeleteView):

    model = Company
    template_name = 'companies/company-delete.html'
    form_class = CompanyDeleteForm

    def get_success_url(self):
        return reverse_lazy('home')

    def user_created_company(self):
        company = get_object_or_404(Company, user=self.request.user)
        return self.request.user == company.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'data': self.get_initial()})
        return kwargs


class CompanyListView(ListView):

    model = Company
    template_name = 'companies/company-list.html'
    context_object_name = 'companies'
    companies = Company.objects.all().order_by('name', 'id')
    paginate_by = 20


