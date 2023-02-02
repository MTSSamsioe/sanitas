from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile(request):
    """
    Show users profiles
    """
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)