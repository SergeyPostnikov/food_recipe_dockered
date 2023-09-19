from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from recipes.models import Category, Recipe
from django.utils import timezone as tz


class Subscription(models.Model):
    class Subscriptions(models.TextChoices):
        FREE = 'FR', _('Бесплатная')
        BASE = 'BS', _('Базовая')
        GOLD = 'GD', _('Золотая')
    
    user = models.ForeignKey(
        'SiteUser',
        related_name='subscription',
        on_delete=models.CASCADE,
    )
    subscription = models.CharField(
        'Тип подписки',
        null=False,
        blank=False,
        max_length=2,
        choices=Subscriptions.choices,
        default=Subscriptions.FREE
    )
    expiration_date = models.DateField(
        'Дата окончания подписки',
        blank=False,
        null=False
    )
    
    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"    

    def __str__(self):
        return f'{self.get_subscription_display()} {self.user} до {self.expiration_date}'

    def is_expired(self):
        if self.expiration_date:
            return self.expiration_date < tz.now()
        return False


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

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return f'{self.user} {self.get_vote_display()}'


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
