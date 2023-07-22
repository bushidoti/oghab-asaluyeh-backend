from django.contrib import admin
from .models import Product, AllProducts, AutoIncrement, Handling, AutoIncrementCheck, AutoIncrementFactor

admin.site.register(Product)
admin.site.register(AllProducts)
admin.site.register(AutoIncrement)
admin.site.register(AutoIncrementCheck)
admin.site.register(Handling)
admin.site.register(AutoIncrementFactor)
