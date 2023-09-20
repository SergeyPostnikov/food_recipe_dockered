from django.shortcuts import render
from .models import SiteUser
# Create your views here.


def login(request):
    return render(request, 'auth.html')


def veiw_lk(request, pk):
    return render(request, 'lk.html')


def make_order(request):
    return render(request, 'order.html')


def register(request):
    return render(request, 'registration.html')
