from django.contrib import admin
from .models import Product, AllProducts, AutoIncrement, Handling, AutoIncrementCheck, AutoIncrementFactor, Consumable

admin.site.register(Product)
admin.site.register(AllProducts)
admin.site.register(AutoIncrement)
admin.site.register(AutoIncrementCheck)
admin.site.register(Handling)
admin.site.register(AutoIncrementFactor)
admin.site.register(Consumable)
