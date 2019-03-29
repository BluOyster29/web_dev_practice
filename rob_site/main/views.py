from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! wWow so £amaze.")
