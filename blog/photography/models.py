from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="similar_listings")
    
    def __str__(self):
        return f"{self.title} - {self.category}"
   
class Picture(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_pictures")
    picture = models.ImageField(upload_to="images/")
    alt_text = models.CharField(max_length=140)
    
class Contact(models.Model):
    Name = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    Details = models.CharField(max_length=2000)
    
    def __str__(self):
        return f"{self.email}"
