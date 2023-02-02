from django.shortcuts import render


def profile(request):
    """
    Show users profiles
    """
    context = {

    }

    return render(request, 'profiles/profile.html', context)