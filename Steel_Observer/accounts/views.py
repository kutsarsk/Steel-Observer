from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Steel_Observer.accounts.forms import AppUserCreationForm, ProfileEditForm
from Steel_Observer.accounts.models import Profile
from Steel_Observer.permissions import SuperPermissionMixin
from Steel_Observer.records.models import Record

UserModel = get_user_model()


class UserLoginView(LoginView):

    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):

    template_name = 'home.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserRegisterView(CreateView):

    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse('profile-edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        user_profile = Profile.objects.create(user=self.object)
        user_profile.save()
        login(self.request, self.object)
        return response


class ProfileDetailsView(LoginRequiredMixin, DetailView):

    model = UserModel
    template_name = 'accounts/profile-details.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.object)
        records = Record.objects.filter(user=self.object).order_by('-date', 'product', 'region', 'type', 'pk')
        paginator = Paginator(records, self.paginate_by)
        page = self.request.GET.get('page')
        context['records'] = paginator.get_page(page)
        context['paginator'] = Paginator(records, self.paginate_by)
        context['page_obj'] = paginator.get_page(page)
        context['is_paginated'] = records.count() > self.paginate_by
        return context


class ProfileEditView(SuperPermissionMixin, UpdateView):

    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ProfileDeleteView(SuperPermissionMixin, DeleteView):

    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('login')

