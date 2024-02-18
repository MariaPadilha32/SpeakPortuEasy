from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')
    #return HttpResponse('Hello World - Welcome to Django Framework')
