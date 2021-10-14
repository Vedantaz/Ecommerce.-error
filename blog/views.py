from django.shortcuts import render
from django.shortcuts import HttpResponse
# import product from models 

def index(request):
    return render(request,"blog/index.html")


