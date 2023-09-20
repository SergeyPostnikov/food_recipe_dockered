from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from recipes.models import Category, Recipe
from django.utils import timezone as tz


class Subscription(models.Model):
    class Durations(models.IntegerChoices):
        ONE = 1, _('Один месяц')
        THREE = 3, _('Три месяца')
        SIX = 6, _('Шесть месяцев')
        TWELVE = 12, _('Двеннадцать месяцев')
    
    user = models.ForeignKey(
        'SiteUser',
        related_name='subscription',
        on_delete=models.CASCADE,
    )
    duration_months = models.IntegerField(
        'Тип подписки',
        null=False,
        blank=False,
        choices=Durations.choices,
        default=Durations.ONE
    )

    start_date = models.DateField(
        'Дата начала подписки',
        blank=False,
        null=False,
        default=tz.now
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
        related_name='allergies', 
        blank=True,
        verbose_name='Аллергии'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
