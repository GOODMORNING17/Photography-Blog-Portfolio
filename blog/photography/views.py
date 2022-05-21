from django.forms import ModelForm, modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.http import JsonResponse

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class newPictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'alt_text']
        
def index(request):
    return render(request, "auctions/index.html")
    
def listing(request, listing_id):
    listing = listing.objects.get(id=listing_id)
    PictureFormSet = modelformset_factory(Picture,
                                        form=newPictureForm, extra=4)
    if request.method == 'POST':  
        imagesForm = PictureFormSet(request.POST, request.FILES,
                               queryset=Picture.objects.none()) 
        if imagesForm.is_valid():  
            imagesForm.save() 
        
        for form in imagesForm.cleaned_data:
            if form:
                picture = form['picture']
                text = form['alt_text']
                newPicture = Picture(listing=listing, picture=picture, alt_text=text)
                newPicture.save() 

    return render(request, "auctions/listing.html",{
        "listing":listing,
         "imageForm": PictureFormSet(queryset=Picture.objects.none()),
    })
            
def activeListings(request):
    
    category_id = request.GET.get("category", None)
    if category_id is None:
        listings = Listing.objects.filter()
    else:
        listings = Listing.objects.filter(category=category_id)
    categories = Category.objects.all()
    for listing in listings:
        listing.mainPicture = listing.get_pictures.first()
    return render(request, "auctions/listing.html", {
        "listings": listings,
        "categories": categories,
        "page_title": "Active Listings"
    })

def about(request):
    return render(request, "auctions/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'auctions/contactsuccess.html')
        else:
            return render(request, 'auctions/contactfailure.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'auctions/contact.html', context)