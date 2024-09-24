from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
    fo_name=models.TextField(max_length=200)
    fo_image=models.ImageField(upload_to='images/', blank=True)
    fo_min=models.IntegerField()
    fo_km=models.IntegerField()
    fo_rating=models.TextField(max_length=100)
    def __str__(self):
        return self.fo_name
class Menu(models.Model):
    name=models.TextField(max_length=100)
    image=models.ImageField(upload_to='images/', blank=True)
    rating=models.TextField(max_length=100)
    price=models.IntegerField()
    review=models.TextField(max_length=200)
    def __str__(self):
        return self.name
class Add(models.Model):
    name=models.ForeignKey(Menu,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
class itemadd(models.Model):
    deliverytime=models.TextField()
    deliveryaddress=models.TextField(max_length=200)
    phonenumber=models.TextField(max_length=100)
    def __str__(self):
        return  str (self.phonenumber)





    

