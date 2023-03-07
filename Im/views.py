from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def navin(request):
    return HttpResponse('<h1><center>hi joynaveen</center></h1>')

def navin_1(request):
    return HttpResponse('<h1><marquee>Naveenjoy very bad boy</marquee></h1>')
