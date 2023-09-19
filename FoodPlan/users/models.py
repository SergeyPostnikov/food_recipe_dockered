from django.db import models

from django.contrib.auth.models import AbstractUser
from recipes.models import Category


class SiteUser(AbstractUser):
    categories = models.ManyToManyField(
        Category, 
        related_name='preferences', 
        blank=True,
        verbose_name='Предпочтения'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
