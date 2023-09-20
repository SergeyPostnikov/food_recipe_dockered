from django.urls import path
from .views import veiw_lk, register, login, make_order

urlpatterns = [
    path('<int:pk>/', veiw_lk, name='user_page'),
    path('register/', register, name='register'),
    path('order/', make_order, name='order'),
    path('login/', login, name='login')
]
 
