
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About-Us"),   
    path("contact/", views.contact, name="Contact-Us"),   
    path("tracker/", views.tracker, name="Tracking Status"),    
    path("search/", views.index, name="Search"),
    path("prodView/", views.prodView, name="prodView"),
    path("checkout/", views.checkout, name="Check Out"),
    path("enter/", views.enter, name="Enter"),
    path("purchase/", views.purchase, name="Purchase"),
    
]
