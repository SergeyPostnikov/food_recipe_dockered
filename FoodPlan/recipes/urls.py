from django.urls import path
from .views import index, get_recipe
from .views import simple_recipe_view, detail_recipe_view


urlpatterns = [
    path('', index, name='index'),
    path('recipe/<int:pk>/', get_recipe, name='recipe'),
    path('simple-recipe/', simple_recipe_view, name='simple-recipe'),
    path('detail-recipe/', detail_recipe_view, name='detail-recipe'),
]
