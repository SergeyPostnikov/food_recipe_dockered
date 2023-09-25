from django.shortcuts import get_object_or_404, render
from .models import Ingredient, Recipe
from users.models import Vote, SiteUser


def get_recipes_element(request):
    allergies = request.user.allergies.all()

    recipes = Recipe.objects.exclude(category=allergies[0])[:3]
    # recipes = Recipe.objects.all()
    
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


def simple_recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    if request.method == 'POST':
        user = get_object_or_404(SiteUser, pk=request.user.pk)
        action = 'L' if request.POST.get('like-button') == '+' else 'D'
        Vote.objects.get_or_create(
                user=user,
                recipe=recipe,
                vote=action,
            )

    likes = len(Vote.objects.filter(vote='L', recipe=recipe))
    dislikes = len(Vote.objects.filter(vote='D', recipe=recipe))
    ingredients = recipe.ingredients.all()
    return render(
        request,
        'card3.html',
        context={
            'recipe': recipe,
            'likes': likes,
            'dislikes': dislikes,
            'ingredients': ingredients
            }
    )


def detail_recipe_view(request):
    recipes_elements = get_recipes_element(request)
    return render(
        request,
        template_name='card2.html',
        context={
            'recipes_elements': recipes_elements
        }
    )
