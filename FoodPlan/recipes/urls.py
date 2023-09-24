from django.urls import path
from .views import index
from .views import simple_recipe_view, detail_recipe_view


urlpatterns = [
    path('', index, name='index'),
    path('simple-recipe/<int:pk>/', simple_recipe_view, name='recipe'),
    path('detail-recipe/', detail_recipe_view, name='detail-recipe'),
]
