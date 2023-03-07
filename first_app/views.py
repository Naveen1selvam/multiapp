from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<center><h1>welcome to Django class</center></h1>')
def second(request):
    return HttpResponse('Virat kohli')