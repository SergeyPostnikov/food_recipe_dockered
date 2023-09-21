from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser


class SiteUserCreationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ['username', 'email', 'password1']
