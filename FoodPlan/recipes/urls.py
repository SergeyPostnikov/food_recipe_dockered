from django.urls import path
from .views import index, get_recipe

urlpatterns = [
    path('', index, name='index'),
    path('recipe/<int:pk>', get_recipe, name='recipe')
]
