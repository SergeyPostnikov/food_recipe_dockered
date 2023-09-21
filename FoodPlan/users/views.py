from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
    
from .models import SiteUser


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('index'))
        else:
            print(form.errors)
            print(request.POST)
    else:
        form = AuthenticationForm()

    return render(request, 'auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def veiw_lk(request, pk):
    user = get_object_or_404(SiteUser, pk=pk)
    return render(
        request, 
        'lk.html',
        context={'user': user}
    )


def make_order(request):
    return render(request, 'order.html')


def register(request):
    return render(request, 'registration.html')
