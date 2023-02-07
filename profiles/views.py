from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

def profile(request):
    """
    Show users profiles
    """
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile is updated')
            else:
                messages.error(request, 'Something went wrong please try again')
        else:
            form = ProfileForm(instance=profile)
        
        context = {
            'form': form,
            
        }

        return render(request, 'profiles/profile.html', context)
    else:
        messages.error(request, 'You must be logged  in to see user  profile. Please lo in or create an account.')
        return redirect('/accounts/login/')