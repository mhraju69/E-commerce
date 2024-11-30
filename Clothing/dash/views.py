from django.shortcuts import render
from shop.models import *
from category.models import *
from django.utils.text import slugify
# Create your views here.

def dash(request):
    products = Product.objects.all().order_by('name')
    cats = Category.objects.all().order_by('name')
    colors = Color.objects.all().order_by('color')
    sizes = Size.objects.all().order_by('size')
    
    if 'new' in request.POST :
        name = request.POST['name']
        slug = slugify(name)
        cat = request.POST['cat']
        price = request.POST['price']
        color = request.POST.getlist('color')
        size = request.POST.getlist('size')
        image = request.FILES['img']
        details = request.POST['details']
        try:
            size.remove('default')
            color.remove('default')
        except: pass
        
        new = Product(name=name,price=price,image=image,slug=slug,stock=5,ditails = details)
        new.category = Category.objects.get(id = cat)
        new.save()
        new.color.add(*color)
        new.size.add(*size)
        
        new.save()
        
        print('name:',name,'   cat',cat,'     price',price,'    color:',color,'     size:',size ,'   image:',image)

                
    
    
    if 'edit' in request.POST :
        product_id = request.POST['product_id']
        new_name = request.POST['new_name']
        new_cat = request.POST['new_cat']
        new_price = request.POST['new_price']
                
        product = Product.objects.get(id= product_id)     
        
        print(new_cat)
        product.name = new_name
        product.category = Category.objects.get(id = new_cat)
        product.price = new_price
        
        print(product.category.id)
        
        product.save()
    
    
    
    context = {
        'product' : products,
        'cat' : cats,
        'colors' :colors,
        'sizes' : sizes
    }
    
    
    return render(request,'dash.html',context)

