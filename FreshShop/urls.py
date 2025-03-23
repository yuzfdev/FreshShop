"""
URL configuration for FreshShop project.

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
from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('register/', views.register),
    path('', views.login),
    path('logout/', views.logout),
    path('products/', views.all_products),
    path('view_cart/', views.view_cart),
    path('add_to_cart/<int:pid>/', views.add_to_cart),
    path('remove_from_cart/<int:id>/', views.remove_from_cart),
    path('update_cart/<int:id>/', views.update_cart),
    path('checkout/', views.checkout)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
