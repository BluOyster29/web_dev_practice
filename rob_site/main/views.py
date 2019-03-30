from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from .models import cars
# Create your views here.

def homepage(request):
    return render(request =request,
                  template_name='main/home.html',
                  context= {"tutorials" : Tutorial.objects.all,
                  "cars" : cars.objects.all})


def about(request):
    return HttpResponse("This is all about me, ROBBY!")

def rob(request):
    return redirect("https://www.facebook.com/BluOyster29")       
    
def nils(request):
    return redirect("https://www.facebook.com/nils.zachmann")
