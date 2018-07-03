from django.shortcuts import render

def index(request):
    return render(request, 'summary/index.html', {})
