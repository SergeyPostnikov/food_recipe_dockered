from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=25
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ingredient(models.Model):
    name = models.CharField(
        'Название', 
        max_length=255
    )
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    amount = models.DecimalField(
        'Количество', 
        max_digits=10, 
        decimal_places=2
    )
    unit = models.CharField(
        'Единица измерения',
        max_length=20        
    )

    def __str__(self):
        return f'{self.name} {self.amount} {self.unit}'

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=50
    )
    category = models.ManyToManyField(
        Category, 
        related_name='recipes'
    )
    text = models.TextField('Рецепт')
    calories = models.IntegerField(
        blank=False, 
        null=False,
        default=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
