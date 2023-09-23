from django.urls import path
from .views import veiw_lk, register, login_view, make_order, logout_view, create_subscribe

urlpatterns = [
    path('<int:pk>/', veiw_lk, name='user_page'),
    path('register/', register, name='register'),
    path('order/', make_order, name='order'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
 
