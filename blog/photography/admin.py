from django.contrib import admin
from .models import Listing, Category, Picture, Contact

# Register your models here.

admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Contact)