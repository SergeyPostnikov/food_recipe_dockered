from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    return render(request, 'index.html')


def get_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'card3.html', context={'recipe': recipe})
