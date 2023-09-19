from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from recipes.models import Category, Recipe


class Vote(models.Model):
    class Votes(models.TextChoices):
        LIKE = 'L', _('Лайк')
        DISLIKE = 'D', _('Дизлайк')

    user = models.ForeignKey(
        'SiteUser',
        related_name='voted_recepies',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='users_voted',
        on_delete=models.CASCADE
    )
    vote = models.CharField(
        'Голос',
        max_length=1,
        choices=Votes.choices,
        default=Votes.LIKE,
        )


class SiteUser(AbstractUser):
    class Subscriptions(models.TextChoices):
        FREE = 'FR', _('Бесплатная')
        BASE = 'BS', _('Базовая')
        GOLD = 'GD', _('Золотая')

    categories = models.ManyToManyField(
        Category, 
        related_name='preferences', 
        blank=True,
        verbose_name='Предпочтения'
    )
    subscription = models.CharField(
        'Подписка',
        null=False,
        blank=False,
        max_length=2,
        choices=Subscriptions.choices,
        default=Subscriptions.FREE
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
