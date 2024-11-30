from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.cart , name='cart'),
    path('add_cart/<int:product_id>/', views.addCart, name='addCart'),
    path('add/<int:product_id>/<str:color>/<str:size>/', views.add ,name='add' ),
    path('delete/<int:product_id>/<str:color>/<str:size>/', views.dell ,name='dell' ),
    path('delete_wish/<int:product_id>/', views.deleteWish ,name='deleteWish' ),
    path('wishlist/', views.wish , name='wish'),
    path('add_wish/<int:product_id>/', views.addWish, name='addWish'),
    ]