from django.contrib import admin
from .models import Category, Brand, Product,ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'status', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
