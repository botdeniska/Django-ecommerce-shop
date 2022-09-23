from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)


# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'data_order', 'complete']
    list_filter = ['customer', 'data_order']


# admin.site.register(OrderItem)
@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'data_added']
    list_filter = ['order']


admin.site.register(ShippingAddress)
