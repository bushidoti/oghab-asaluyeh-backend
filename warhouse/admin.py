from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'scale', 'inventory']
    list_editable = ['name', 'category', 'scale', 'inventory']
    list_per_page = 10
    actions_on_bottom = False
    list_filter = ['category', 'inventory']
    search_fields = (
        "code",
        "name",
    )


class AllProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'category', 'document_type', 'systemID',
                    'document_code', 'date', 'operator', 'scale', 'operator', 'afterOperator', 'consumable',
                    'buyer', 'seller', 'receiver', 'amendment', 'inventory']
    actions_on_bottom = False
    list_per_page = 20
    list_filter = ['consumable', 'operator', 'document_type', 'product__inventory', 'product__category']
    search_fields = (
        "product__code",
        "product__name",
        "systemID"
    )


class FactorsProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'inventory']
    actions_on_bottom = False
    list_per_page = 20
    list_filter = ['inventory']
    search_fields = (
        "code",
    )


class ProductCheckAdmin(admin.ModelAdmin):
    list_display = ['code', 'inventory']
    actions_on_bottom = False
    list_per_page = 20
    list_filter = ['inventory']
    search_fields = (
        "code",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(AllProducts, AllProductsAdmin)
admin.site.register(AutoIncrement)
admin.site.register(AutoIncrementCheck)
admin.site.register(Handling)
admin.site.register(AutoIncrementFactor)
admin.site.register(Consumable)
admin.site.register(Category)
admin.site.register(AutoIncrementProductFactor)
admin.site.register(AutoIncrementProduct)
admin.site.register(FactorsProduct, FactorsProductAdmin)
admin.site.register(AutoIncrementProductCheck)
admin.site.register(ProductCheck, ProductCheckAdmin)
admin.site.register(Transmission)
