from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Steel_Observer.accounts.forms import AppUserCreationForm, ProfileEditForm
from Steel_Observer.accounts.models import Profile

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.object)
        return context


class ProfileEditView(UpdateView):

    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def own_profile(self):
        user_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == user_profile.user

    # def get_object(self, queryset=None):
    #     return self.request.user

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ProfileDeleteView(DeleteView):

    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('login')

    def own_profile(self):
        user_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == user_profile.user
