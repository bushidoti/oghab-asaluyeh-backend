from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from authentification.views import *
from documentManagement.views import DocumentApi
from propertyManagement.views import PersonApi, MovableApi, ImmovableApi
from warhouse.views import *
from property.views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'documents', DocumentApi, 'documents')
router.register(r'persons', PersonApi, 'persons')
router.register(r'employee', EmployeeApi, 'employee')
router.register(r'user', UserApi, 'user')
router.register(r'product', ProductApi, 'product')
router.register(r'allproducts', AllProductstApi, 'allproducts')
router.register(r'movable', MovableApi, 'movable')
router.register(r'immovable', ImmovableApi, 'immovable')
router.register(r'autoincrement_property', AutoIncrementPropertyApi, 'autoincrement_property')
router.register(r'banner', BannerApi, 'banner')
router.register(r'checksproduct', ChecksProductApi, 'checksproduct')
router.register(r'transmission', TransmissionApi, 'transmission')
router.register(r'autoincrementproductcheck', AutoIncrementProductCheckApi, 'autoincrementproductcheck')
router.register(r'consumable-list', ConsumableApi, 'consumable-list')
router.register(r'autoincrementproduct', AutoIncrementProductApi, 'autoincrementproduct')
router.register(r'autoincrementproductfactor', AutoIncrementProductFactorApi, 'autoincrementproductfactor')
router.register(r'factorsproduct', FactorsProductApi, 'factorsproduct')
router.register(r'category-list', CategoryApi, 'category-list')
router.register(r'factor_property', FactorPropertyApi, 'factor_property')
router.register(r'maintenance', MaintenanceApi, 'maintenance')
router.register(r'autoincrement_property_factor', AutoIncrementPropertyFactorApi, 'autoincrement_property_factor')
router.register(r'handling-product', HandlingApi, 'handling-product')
router.register(r'property', PropertyApi, 'property')
router.register(r'repaired_property', RepairedPropertyApi, 'repaired_property')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('token/',
                       jwt_views.TokenObtainPairView.as_view(),
                       name='token_obtain_pair'),
                  path('token/refresh/',
                       jwt_views.TokenRefreshView.as_view(),
                       name='token_refresh'),
                  path('', include('authentification.urls')),
                  path('api/', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
