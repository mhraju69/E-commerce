from django.contrib import admin
from.models import *
# Register your models here.
class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','category','stock')
    list_filter = ('category',)
    
admin.site.register(Product,productAdmin)

admin.site.register(Color)
admin.site.register(Size)