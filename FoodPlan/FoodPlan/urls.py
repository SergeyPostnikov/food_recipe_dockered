from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render, kwargs={'template_name': 'index.html'}, name='start_page'),
    path('recipes/', include('recipes.urls')),
    path('user/', include('users.urls')),
]
