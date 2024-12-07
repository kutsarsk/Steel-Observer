from django.urls import path, include

from Steel_Observer.companies import views


urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company-list'),
    path('create/', views.CompanyCreateView.as_view(), name='company-create'),
    path('<int:pk>/', include([
        path('details/', views.CompanyDetailsView.as_view(), name='company-details'),
        path('edit/', views.CompanyEditView.as_view(), name='company-edit'),
        path('delete/', views.CompanyDeleteView.as_view(), name='company-delete'),
    ]),)
]
