from urllib import request
from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'bootstrap.html')

def cdn_bootstrap(request):
    return render(request,'cdn_bootstrap.html')