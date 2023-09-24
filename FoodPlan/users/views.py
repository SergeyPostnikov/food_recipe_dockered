from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SiteUserCreationForm
    
from .models import SiteUser, Subscription


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


@login_required
def veiw_lk(request, pk):
    user = get_object_or_404(SiteUser, pk=pk)
    subscription = Subscription.objects.filter(user=user).first()
    context = {
        'subscription': subscription,
        'user': user
    }
    return render(
        request, 
        'lk.html',
        context
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


def create_subscribe(request):

    email = request.GET.get('EMAIL')
    address = request.GET.get('ADDRESS')
    order_date = request.GET.get('DATE')
    order_time = request.GET.get('TIME')
    comment = request.GET.get('DELIVCOMMENTS')
    customer_name = request.GET.get('NAME')
    cake_name = request.GET.get('COMMENTS')
    phone = request.GET.get('PHONE')
    inscription=request.GET.get('WORDS')
    levels = request.GET.get('LEVELS')
    form = request.GET.get('FORM')
    topping = request.GET.get('TOPPING')
    berries = request.GET.get('BERRIES')
    decor = request.GET.get('DECOR')
    cake_id = request.GET.get('CAKE')
    total_cost = 0
    cake_berries_obj = None
    cake_decor_obj = None
    if berries:
        cake_berries_obj = Berries.objects.get(id=berries)
        total_cost += cake_berries_obj.price
    if decor:
        cake_decor_obj = Decors.objects.get(id=decor)
        total_cost += cake_decor_obj.price
    if inscription:
        total_cost = total_cost + 500

    if not id:
        cake_form_obj = Forms.objects.get(id=form)
        cake_levels_obj = Sizes.objects.get(id=levels)
        cake_topping_obj = Toppings.objects.get(id=topping)
        total_cost += int(cake_form_obj.price + cake_levels_obj.price + cake_topping_obj.price)
        if order_date:
            order_date_dtobj = datetime.datetime.strptime(order_date, '%Y-%m-%d')
            min_date = datetime.datetime.now() + datetime.timedelta(days=1)
            if order_date_dtobj < min_date:
                total_cost = int(total_cost) * 1.2

        order = Order.objects.create(
            client_name=customer_name,
            phonenumber=phone,
            email=email,
            comment=cake_name,
            address=address,
            delivery_datetime=f'{order_date} {order_time}',
            delivery_comment=f'{comment}',
            order_receipt_method='DELIVERY',
            cake_size=cake_levels_obj,
            cake_form=cake_form_obj,
            cake_topping=cake_topping_obj,
            cake_berry=cake_berries_obj,
            cake_decor=cake_decor_obj,
            inscription=inscription,
            total_cost=total_cost
        )

    else:
        cake = CatalogCake.objects.get(id=cake_id)
        total_cost += int(cake.price)

        if order_date:
            order_date_dtobj = datetime.datetime.strptime(order_date, '%Y-%m-%d')
            min_date = datetime.datetime.now() + datetime.timedelta(days=1)
            if order_date_dtobj < min_date:
                total_cost = int(total_cost) * 1.2

        order = Order.objects.create(
            client_name=customer_name,
            phonenumber=phone,
            email=email,
            comment=cake_name,
            address=address,
            delivery_datetime=f'{order_date} {order_time}',
            delivery_comment=f'{comment}',
            order_receipt_method='DELIVERY',
            cake_berry=cake_berries_obj,
            cake_decor=cake_decor_obj,
            inscription=inscription,
            total_cost=total_cost,
        )
        OrderCatalogCakes.objects.create(
            order=order,
            catalog_cake=cake,
            quantity=1,
            price=cake.price
        )