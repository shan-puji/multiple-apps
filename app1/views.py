from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Sanvi(request):
    return HttpResponse('<h1>Self love-best</h1>')
def Mini(request):
    return HttpResponse('<h1>I am learning Django</h1>')
def Baby(request):
    return HttpResponse('<h1>I Love You Amma')