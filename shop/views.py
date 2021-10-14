from django import http
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product
from math import ceil 
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    params ={'no_of_slides ': nSlides,'range':range(1, nSlides),  'products': products}
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,"shop/about.html")
    
def contact(request):
    return HttpResponse("We are at contact")
    
def tracker(request):
    return HttpResponse("We are at tracker")
    
def search(request):
    return HttpResponse("We are at search")
    
def prodView(request):
    return HttpResponse("We are at productview")
    
def checkout(request):
    return HttpResponse("We are at checkout")
     
def enter(request):
    return HttpResponse("We have successfully entered")
     
def purchase(request):
    return HttpResponse("We are at Purchase Phasse")












