from django.contrib import admin
from .models import*
# Register your models here.
class cartitemmanager(admin.ModelAdmin):
    list_display = ('product' , 'color' , 'size', 'quantity')
    list_filter = ( 'color' , 'size', 'quantity')

admin.site.register(CartItems,cartitemmanager)
admin.site.register(WishItem)

