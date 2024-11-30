from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField( upload_to='category/image', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    def url(self):
        return reverse('products_by_category',args=[self.slug])
    