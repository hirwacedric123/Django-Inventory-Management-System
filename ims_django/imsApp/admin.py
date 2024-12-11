from django.contrib import admin
from imsApp.models import Category, Product, Stock, Invoice, Invoice_Item
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Stock)
# admin.site.register(Invoice)
# admin.site.register(Invoice_Item)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'date_created', 'date_updated')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'price', 'status', 'date_created', 'date_updated')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'type', 'date_created', 'date_updated')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction', 'customer', 'total', 'date_created', 'date_updated')

@admin.register(Invoice_Item)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'product', 'stock', 'price', 'quantity')