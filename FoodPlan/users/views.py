from django.shortcuts import render, get_object_or_404, redirect

# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SiteUserCreationForm
    
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
    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))
    
    if request.method == 'POST':
        form = SiteUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index')
    else:
        form = SiteUserCreationForm()    
    return render(
        request, 
        'registration.html',
        context={'form': form}
    )
