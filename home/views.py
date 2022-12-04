from django.shortcuts import render
from home.models import Destination


def home(request):
    
    dests=Destination.objects.all()
    return render(request,'home.html',{'dests':dests})