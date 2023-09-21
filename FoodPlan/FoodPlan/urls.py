from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render, kwargs={'template_name': 'index.html'}, name='start_page'),
    path('recipes/', include('recipes.urls')),
    path('user/', include('users.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
