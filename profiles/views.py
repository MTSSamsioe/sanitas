from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm


def profile(request):
    """
    Show users profiles
    """
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)