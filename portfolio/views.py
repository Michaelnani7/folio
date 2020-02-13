from django.shortcuts import render
from .models import Portfolio

# Create your views here.


def index(request):
    port = Portfolio.objects.all()
    context ={
        'port': port
    }
    return render(request, 'portfolio/index.html', context)
