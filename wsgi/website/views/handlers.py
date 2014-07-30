__author__ = 'adonis'


from django.contrib import messages
from django.shortcuts import redirect


def handle404(request):
    messages.error(request, "The requested page was not found.")
    return redirect('special:broken')


def handle500(request):
    messages.error(request, "An error has occurred on the server.")
    return redirect('home:index')
