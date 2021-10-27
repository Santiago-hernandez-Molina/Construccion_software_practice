from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    return render(request,'characters/index.html')

def save(request):
    return render(request,'characters/save.html')

def detail(request):
    return render(request,'characters/detail.html')
 