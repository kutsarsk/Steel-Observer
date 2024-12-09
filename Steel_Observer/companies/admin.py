from django.contrib import admin


from Steel_Observer.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'business_field', 'products', 'user')
    search_fields = ('name', 'location', 'business_field', 'products', 'user')
    list_filter = ('name', 'location', 'business_field', 'products', 'user')

