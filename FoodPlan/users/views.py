from django.utils import timezone as tz

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SiteUserCreationForm
    
from .models import SiteUser, Subscription
from recipes.models import Category


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('index'))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', reverse_lazy('index'))
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required(login_url='/user/login')
def veiw_lk(request, pk):
    user = get_object_or_404(SiteUser, pk=pk)
    subscription = Subscription.objects.filter(user=user).first()
    allergies = user.allergies.all()
    context = {
        'subscription': subscription,
        'user': user,
        'allergies': allergies
    }
    return render(
        request, 
        'lk.html',
        context
    )


def make_order(request):
    if request.method == 'POST':
        return redirect('payment')

    allergies = Category.objects.filter(is_allergy=True)
    return render(
        request, 
        'order.html',
        context={'allergies': allergies}
    )


@login_required(login_url='/user/login')
def payment(request):
    if request.method == 'GET':
        user = get_object_or_404(SiteUser, pk=request.user.pk)        
        duration = int(request.GET.get('duration', '1'))
        days = 30 * duration
        expiration_date = tz.now() + tz.timedelta(days=days)

        allergy_pk = request.GET.get('allergy', '')
        another_allergy = request.GET.get('another_allergy', '')

        if allergy_pk:
            allergy = Category.objects.get(pk=int(allergy_pk))
            user.allergies.add(allergy)
        
        if another_allergy:
            allergy, _ = Category.objects.get_or_create(
                pk=allergy_pk, 
                defaults={
                    'name': another_allergy, 
                    'is_allergy': True
                }
            )
            user.allergies.add(allergy)

        subscription = Subscription(
            user=user,
            expiration_date=expiration_date,
            duration_months=duration
        )
        subscription.save()

    if request.method == 'POST':
        return redirect('user_page', pk=request.user.pk)
    return render(request, 'payment.html')


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
