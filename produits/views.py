
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html.twig', {})
    
# Create your views here.
def hello(request):
    text = "<h1>Hello world</h1><p>Benjoueuuuuur</p>"
    return HttpResponse(text)

def result(request, number):
    text = "lez goooo %d"%number
    return HttpResponse(text)

