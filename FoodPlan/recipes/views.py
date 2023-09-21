from django.shortcuts import get_object_or_404, render

from .models import Ingredient, Recipe


def get_recipes_element():
    recipes = Recipe.objects.all()
    recipes_list = {}
    for item in recipes:
        ingredients = Ingredient.objects.filter(recipe_id=item.id)
        recipes_list[item.id] = {
            'title': item.title,
            'calories': item.calories,
            'text': item.text,
            'ingredients': {ingredient.id: f'{ingredient.name} ({ingredient.amount}{ingredient.unit})' for ingredient in
                            ingredients}
        }
    return recipes_list


def index(request):
    return render(
        request,
        'index.html',
        context={'user': request.user}
    )


def get_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(
        request,
        'card3.html',
        context={'recipe': recipe}
    )


def simple_recipe_view(request):
    return render(request, 'card1.html')


def detail_recipe_view(request):
    recipes_elements = get_recipes_element()
    return render(
        request,
        template_name='card2.html',
        context={
            'recipes_elements': recipes_elements
        }
    )
