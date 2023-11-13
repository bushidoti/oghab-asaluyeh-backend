from django.contrib import admin
from .models import *


class AutoIncrementPropertyAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'name', 'increment']
    list_filter = ['inventory']
    list_editable = ['increment']


class FactorPropertyAdmin(admin.ModelAdmin):
    list_display = ['code', 'inventory']
    list_per_page = 20
    list_filter = ['inventory']
    search_fields = (
        "code",
    )


class AutoIncrementPropertyFactorAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'increment']
    list_filter = ['inventory']
    list_editable = ['increment']


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'user', 'using_location', 'number', 'type_furniture', 'year_made', 'owner',
                    'use_for',
                    'year_buy', 'repaired_status', 'install_location', 'document_code', 'category',
                    'dst_inventory', 'model', 'sub_item_type', 'property_number', 'inventory']

    list_per_page = 20
    list_filter = ['category', 'inventory', 'sub_item_type', 'type_furniture']
    search_fields = (
        "code",
        "name",
        "user",
        "using_location",
        'model',
        'document_code',
        'use_for',
        'install_location',
        'year_made',
        'owner',
    )


admin.site.register(AutoIncrementProperty, AutoIncrementPropertyAdmin)
admin.site.register(AutoIncrementPropertyFactor, AutoIncrementPropertyFactorAdmin)
admin.site.register(FactorProperty, FactorPropertyAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(RepairedProperty)
