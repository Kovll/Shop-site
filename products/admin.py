from django.contrib import admin

from products.models import ProductsCategory, Products, Basket
# Register your models here.

admin.site.register(ProductsCategory)
admin.site.register(Basket)

#Настройка админки
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name',)

#Управление корзиной
class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product','created_timestamp',)
    extra = 0
