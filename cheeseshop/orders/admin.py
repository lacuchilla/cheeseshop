from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'units')

admin.site.register(Item, ItemAdmin)

#class StoreAdmin(admin.ModelAdmin):
#    list_display = ('name', 'managerFirstName')

#admin.site.register(Store, StoreAdmin)

#class OrderAdmin(admin.ModelAdmin):
#    list_display = ('orderDate', 'fillDate', 'closedDate')

#admin.site.register(Order, OrderAdmin)
