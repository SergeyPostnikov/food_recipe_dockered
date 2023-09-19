from django.contrib import admin
from .models import SiteUser, Vote, Subscription


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 0


class UserInline(admin.TabularInline):
    model = SiteUser
    extra = 0


@admin.register(SiteUser)
class UserAdmin(admin.ModelAdmin):
    exclude = (
        'last_login', 
        'groups', 
        'user_permissions',
        'date_joined',
        'first_name',
        'last_name',
        # 'email',
        'is_superuser',
        'is_active',
        'is_staff',
        'password'
    )

    inlines = [
        VoteInline,
        SubscriptionInline,
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [
        # UserInline,
    ]
