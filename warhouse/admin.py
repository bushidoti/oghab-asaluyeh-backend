from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'scale', 'inventory']
    list_editable = ['name', 'category', 'scale', 'inventory']
    list_per_page = 10
    list_filter = ['category', 'inventory']
    search_fields = (
        "code",
        "name",
    )


class AllProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'category', 'document_type', 'systemID',
                    'document_code', 'date', 'operator', 'scale', 'operator', 'afterOperator', 'consumable',
                    'buyer', 'seller', 'receiver', 'amendment', 'inventory']
    list_per_page = 20
    list_filter = ['consumable', 'operator', 'document_type', 'product__inventory', 'product__category']
    search_fields = (
        "product__code",
        "product__name",
        "systemID"
    )


class FactorsProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'inventory']
    list_per_page = 20
    list_filter = ['inventory']
    search_fields = (
        "code",
    )


class ProductCheckAdmin(admin.ModelAdmin):
    list_display = ['code', 'inventory']
    list_per_page = 20
    list_filter = ['inventory']
    search_fields = (
        "code",
    )


class AutoIncrementProductAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'increment']
    list_filter = ['inventory']
    list_editable = ['increment']


class AutoIncrementProductFactorAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'increment']
    list_filter = ['inventory']
    list_editable = ['increment']


class AutoIncrementProductCheckAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'increment']
    list_filter = ['inventory']
    list_editable = ['increment']


class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'sender', 'receiver', 'input', 'scale', 'date', 'category', 'systemID']
    list_per_page = 20
    list_filter = ['category']
    search_fields = (
        "name",
        "sender",
        "receiver",
        "systemID",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(AllProducts, AllProductsAdmin)
admin.site.register(AutoIncrement)
admin.site.register(AutoIncrementCheck)
admin.site.register(Handling)
admin.site.register(AutoIncrementFactor)
admin.site.register(Consumable)
admin.site.register(Category)
admin.site.register(AutoIncrementProductFactor, AutoIncrementProductFactorAdmin)
admin.site.register(AutoIncrementProduct, AutoIncrementProductAdmin)
admin.site.register(FactorsProduct, FactorsProductAdmin)
admin.site.register(AutoIncrementProductCheck, AutoIncrementProductCheckAdmin)
admin.site.register(ProductCheck, ProductCheckAdmin)
admin.site.register(Transmission, TransmissionAdmin)
