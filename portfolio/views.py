from django.shortcuts import render
from .models import Photo
import os

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    category = os.path.basename(request.path).capitalize()
    context = {
        'page_title': "- " + category,
        'photos': Photo.objects.filter(category=category),
        'category': category
    }
    return render(request, 'portfolio.html', context=context)