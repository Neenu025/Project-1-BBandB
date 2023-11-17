from django.contrib import admin

# Register your models here.

from .models import Customer , Product, Category
from SHOPPER.models import Cart , Wishlist , Address , Order , Coupon




admin.site.register(Customer)

admin.site.register(Product)

admin.site.register(Category)

admin.site.register(Wishlist)

admin.site.register(Address)

admin.site.register(Order)

admin.site.register(Coupon)



