from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from recipes.models import Category


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
