
from django.shortcuts import render
from django.conf import settings

def index(request):
    """ A view to return the index page """
    GOOGLEKEY = settings.GOOGLEMAPS_KEY
    
    context = {
        'GOOGLEKEY': GOOGLEKEY,
    }
    
    return render(request, 'home/index.html', context)


