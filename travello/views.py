from django.shortcuts import render
from django.http import HttpResponse
from.models import Destination


def index(request):

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests': dests})
'''
def Mumbai(request):
    return render(request,'Mumbai.html')

def Hyderabad(request):
    return render(request,'Hyderabad.html')

def Pune(request):
    return render(request,'Pune.html')

def Bangalore(request):
    return render(request,'Bangalore.html')

def Delhi(request):
    return render(request,'Delhi.html')
    '''