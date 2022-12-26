from django.shortcuts import render


def home(request):
    return render(request, 'stream/home.html')


def stream(request, uid):
    return render(request, 'stream/stream.html')
