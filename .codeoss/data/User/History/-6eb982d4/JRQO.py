from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def source(request):
    return render(request, 'source.html')



