"""
URL configuration for Steel_Observer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from Steel_Observer.common.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('Steel_Observer.accounts.urls')),
    path('companies/', include('Steel_Observer.companies.urls')),
    path('events/', include('Steel_Observer.events.urls')),
    path('products/', include('Steel_Observer.products.urls')),
    path('records/', include('Steel_Observer.records.urls')),
]


def custom_permission_denied_view(request, exception=None):
    return render(request, '403.html', status=403)


handler403 = custom_permission_denied_view
