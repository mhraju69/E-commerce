from django.shortcuts import render, get_object_or_404
from category.models import *
from cart.views import _cartid
from .models import *
from django.core.paginator import Paginator
from cart.models import *
from django.db.models import Q

# Create your views here.


def shop(request,category_slug=None):
    category = None
    product = None
    sortby = request.GET.get('sort','name_asc')
    order = {
            'name_asc': 'name',
            'name_desc': '-name',
            'price_asc': 'price',
            'price_desc': '-price',
            'created_at_asc': 'created_at',
            'created_at_desc': '-created_at',
        }

    if category_slug != None:
        category = get_object_or_404(Category,slug = category_slug)
        product = Product.objects.filter(category = category , isAvilable = True).order_by(order.get(sortby))
        paginator = Paginator(product, 6)  # প্রতিটি পৃষ্ঠায় ৫টি প্রোডাক্ট
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        count = product.count()
    else:
                
        product = Product.objects.all().order_by(order.get(sortby))
        count = product.count()
        paginator = Paginator(product, 6)  # প্রতিটি পৃষ্ঠায় ৫টি প্রোডাক্ট
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        
    category = Category.objects.all().order_by('name')
    context = {
        'cat' : category,
        'count':count,
        'product' : page_obj,
        'sortby' : sortby,
        'category_slug' :category_slug
    }
    
    return render(request,'home.html',context)


def product(request,product_slug,category_slug):
    
    try :
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        cart = Cart.objects.get(cart_id = _cartid(request))
        cartitem = CartItems.objects.filter(cart = cart)

    except:
        pass
    
    category = Category.objects.get(slug=category_slug)
    related_product = Product.objects.filter(category=category).exclude(slug = product_slug)[:4]
    
    
    context = {
        'product' : product,
        'related_product' : related_product,

        
    }

    return render(request,'product.html',context)


def search(request):
    keyword = request.GET['keyword']
    if keyword:
        product = Product.objects.filter(Q(name__icontains=keyword) | Q(ditails__icontains=keyword))
    count = product.count()
    context ={
        'product' : product,
        'count' : count,
        'category_slug' : keyword
    }
    return render(request,'home.html',context)
    



