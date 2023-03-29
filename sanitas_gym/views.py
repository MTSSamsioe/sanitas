from django.shortcuts import render


def page_not_found(request, exception):
    ''' View to handle custom 404 error code'''

    return render(request, 'page_not_found.html')


def server_error(request):
    ''' View to handle custom 500 error code'''

    return render(request, 'server_error.html')
