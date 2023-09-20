from django.shortcuts import render, get_object_or_404
from .models import SiteUser
# Create your views here.


def login(request):
    return render(request, 'auth.html')


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
