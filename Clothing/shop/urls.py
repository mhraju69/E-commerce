from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.shop , name='shop'),
    path('category=<slug:category_slug>/',views.shop,name='products_by_category'),
    path('category=<slug:category_slug>/product=<slug:product_slug>/', views.product, name='product'),
    path('search/', views.search , name='search')

]
