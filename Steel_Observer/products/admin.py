from django.contrib import admin

from Steel_Observer.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'description', 'user')
    list_filter = ('name', 'user')
