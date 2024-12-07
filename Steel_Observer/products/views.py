from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from Steel_Observer.products.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):

    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-list')


class ProductDetailsView(DetailView):

    model = Product
    template_name = 'products/product-details.html'
    context_object_name = 'product'

    def user_created_product(self):
        product = get_object_or_404(Product, user=self.request.user)
        return self.request.user == product.user

    def get_related_records(self):
        product = self.get_object()
        return product.record_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product'] = self.get_object()
        context['records'] = self.get_related_records().order_by('-date', 'region', 'type', 'pk')
        return context

    paginate_by = 10


class ProductEditView(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductEditForm
    template_name = 'products/product-edit.html'

    def user_created_product(self):
        product = get_object_or_404(Product, user=self.request.user)
        return self.request.user == product.user

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-details', kwargs={'pk': self.request.user.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):

    model = Product
    template_name = 'products/product-delete.html'
    form_class = ProductDeleteForm

    def get_success_url(self):
        return reverse_lazy('home')

    def user_created_product(self):
        product = get_object_or_404(Product, user=self.request.user)
        return self.request.user == product.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'data': self.get_initial()})
        return kwargs


class ProductListView(ListView):

    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    products = Product.objects.all().order_by('name')
    paginate_by = 20
