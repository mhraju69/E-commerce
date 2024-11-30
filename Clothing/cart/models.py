from django.db import models
from shop.models import *

# Create your models here.

class Cart(models.Model):
    
    cart_id = models.CharField(max_length=200,blank=True)
    date = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
class CartItems(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.IntegerField(default=0)
    color = models.CharField(max_length=50,blank=True)
    size = models.CharField(max_length=50,blank=True)


    
    def __str__(self):
        return str(self.product)
    
class WishItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product)
    

    
     
