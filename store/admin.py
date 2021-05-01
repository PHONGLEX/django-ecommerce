# from django.contrib import admin
#
# from .models import Category, Product
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug']
# 	prepopulated_fields = { 'slug': ('name',)}
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ['title', 'author', 'slug', 'price',
# 	                'in_stock', 'created', 'updated']
# 	list_filter = ['in_stock', 'is_active']
# 	list_editable = ['price', 'in_stock']
# 	prepopulated_fields = {'slug': ('title',)}
from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductType,
    ProductSpecification,
    ProductSpecificationValue
)

admin.site.register(Category, MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline
    ]