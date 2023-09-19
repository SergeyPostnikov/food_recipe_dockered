from functools import wraps
from django.shortcuts import redirect


def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.subscription or request.user.subscription.is_expired():
            return redirect('payment_page')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
