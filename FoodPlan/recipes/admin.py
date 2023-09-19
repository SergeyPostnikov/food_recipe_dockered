from django.contrib import admin
from .models import Recipe, Category, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1  


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]  
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe', 'amount', 'unit')
    list_filter = ('recipe__category', 'unit')
    search_fields = ('name', 'recipe__title', 'recipe__category__name')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
