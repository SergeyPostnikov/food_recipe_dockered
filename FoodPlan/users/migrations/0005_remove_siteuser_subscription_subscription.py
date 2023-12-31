# Generated by Django 4.2.5 on 2023-09-19 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='subscription',
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription', models.CharField(choices=[('FR', 'Бесплатная'), ('BS', 'Базовая'), ('GD', 'Золотая')], default='FR', max_length=2, verbose_name='Тип подписки')),
                ('expiration_date', models.DateField(verbose_name='Дата окончания подписки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
