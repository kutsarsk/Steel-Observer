from django.urls import path, include

from Steel_Observer.products import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', include([
         path('', views.ProductDetailsView.as_view(), name='product-details'),
         path('edit/', views.ProductEditView.as_view(), name='product-edit'),
         path('delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    ]))
]
