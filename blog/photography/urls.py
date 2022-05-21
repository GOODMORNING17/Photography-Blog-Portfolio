from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("active", views.activeListings, name="activeListings"),
    path("active/<int:category_id>", views.activeListings, name="activeListings"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]