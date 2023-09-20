from django.contrib import admin
from .models import Recipe, Category, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  


class RecipeInline(admin.TabularInline):
    model = Recipe.category.through
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]  
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
