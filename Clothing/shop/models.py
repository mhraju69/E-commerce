from django.db import models
from category.models import *
# Create your models here.

class Color(models.Model):
    
    color = models.CharField(max_length=50 ,null=True,blank=True)
    
    def __str__(self):
        return self.color
    
    
class Size(models.Model):  
    size = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.size

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product/image')
    ditails = models.TextField()
    color =  models.ManyToManyField(Color,null=True,blank=True)
    size = models.ManyToManyField(Size,null=True,blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    isAvilable = models.BooleanField(default=True)
    
    def url(self):
        return reverse('product',args=[self.category.slug ,self.slug])
    
    

    
    