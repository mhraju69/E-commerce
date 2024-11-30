from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from shop.models import *
from .models import *
# Create your views here.
def _cartid(request):
    cart = request.session.session_key
    
    if not cart:
        cart = request.session.create()
    return cart

def cart(request):
    try:
        cart = Cart.objects.get(cart_id= _cartid(request))
        cart_item = CartItems.objects.filter(cart = cart)
        
        total = 0
        
        for item in cart_item:
            total += item.product.price * item.quantity
            quantity = item.quantity
            
        
        context = {
            'total': total,
            'quantity': quantity,
            'cart_item': cart_item
        }
    except:
        cart_item = []
        total = 0
        quantity = 0
        
        context = {
            'total': total,
            'quantity': quantity,
            'cart_item': cart_item
        }
        
    return render(request,'cart.html',context)




def addCart(request, product_id):
    size=color='Not Seleced'
    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')   
        # প্রোডাক্ট খুঁজে বের করা
    product = get_object_or_404(Product, id=product_id)
        
        # কার্ট খুঁজে বের করা বা তৈরি করা
    cart, created = Cart.objects.get_or_create(cart_id=_cartid(request))
        
        # কার্ট আইটেম খুঁজে বের করা বা তৈরি করা
    same_cart_item = CartItems.objects.filter(
            product=product,
            cart=cart,
            size =size ,
            color = color,
        )
        
    if same_cart_item.exists():
            # যদি আইটেম আগে থেকেই থাকে, পরিমাণ বাড়ানো
            item = same_cart_item.first()
            item.quantity += 1
            item.product.subtotal = item.product.price * item.quantity
            item.save()

    else:
        new_cart_item =CartItems(
            
            product=product,
            cart=cart,
            size =size ,
            color = color,
            subtotal = product.price
            
        )
        new_cart_item.save()
        
        
    return redirect('shop')  # 'shop' নামক URL পাথ



    
    
def add(request,product_id,color,size):
    cart = Cart.objects.get(cart_id= _cartid(request))
    product = Product.objects.get(id = product_id)
    cart_item = CartItems.objects.get(product=product, cart = cart,color=color,size=size)
    cart_item.quantity +=1
    cart_item.subtotal = cart_item.quantity * cart_item.product.price
    cart_item.save()
    
    return redirect('/cart/')
    
    
    
    
    
    
def dell(request,product_id,color,size):
    cart = Cart.objects.get(cart_id= _cartid(request))
    product = Product.objects.get(id = product_id)
    cart_item = get_object_or_404(CartItems, product=product, color=color, size=size,cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.subtotal = cart_item.quantity * cart_item.product.price
        cart_item.save()
    else :
        cart_item.delete()
    
    return redirect('/cart/')

def addWish(request,product_id):
    product = Product.objects.get(id = product_id)
    cart,created = Cart.objects.get_or_create(cart_id= _cartid(request))
    wishItem,created = WishItem.objects.get_or_create(product = product,cart=cart)
    
    wishItem.save()
    return redirect('/shop/')
    
    
    
    
    
def wish(request):
    try:
        cart = Cart.objects.get(cart_id= _cartid(request))
        cart_item = CartItems.objects.filter(cart=cart)
        
        wishItem = WishItem.objects.filter(cart=cart)
        x = []
        for item in wishItem:
            
            if cart_item.filter(product=item.product).exists():
                x.append(item.product)

        
        context = {
              'wishItem' : wishItem,
              
              'x':x
        }
        print(x)
    except:
        wishItem = []
        context = {
        }
    return render(request,'wishlist.html',context)



def deleteWish(request, product_id):
    cart = Cart.objects.get(cart_id=_cartid(request))

    product = Product.objects.get(id=product_id)

    
    try:
        wish_item = WishItem.objects.get(product=product, cart=cart)
        print(wish_item)
        wish_item.delete()
        print("Wish item deleted successfully.")
    except WishItem.DoesNotExist:
        print('WishItem not found.')
    except Exception as e:
        print(f'Error occurred: {e}')
        
    return redirect('/wishlist/')
