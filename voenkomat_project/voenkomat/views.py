from django.shortcuts import render
from .models import Conscript

def index(request):
    return render(request, 'voenkomat/index.html')

def conscript_list(request):
    conscripts = Conscript.objects.all()
    return render(request, 'voenkomat/conscript_list.html', {'conscripts': conscripts})