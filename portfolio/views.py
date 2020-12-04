from django.shortcuts import render
import os

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    print(request.path)
    title = "- " + os.path.basename(request.path).capitalize()
    return render(request, 'portfolio.html', {'page_title': title})