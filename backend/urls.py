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
router.register(r'autoIncrement', AutoIncrementApi, 'autoIncrement')
router.register(r'autoIncrementcheck', AutoIncrementCheckApi, 'autoIncrementcheck')
router.register(r'autoIncrementfactor', AutoIncrementFactorApi, 'autoIncrementfactor')
router.register(r'autoincrementproperty', AutoIncrementPropertyApi, 'autoincrementproperty')
router.register(r'airportequipment', AirportEquipmentApi, 'airportequipment')
router.register(r'safetyequipment', SafetyEquipmentApi, 'safetyequipment')
router.register(r'airportvehicle', AirportVehicleApi, 'airportvehicle')
router.register(r'airplane', AirplaneApi, 'airplane')
router.register(r'officevehicle', OfficeVehicleApi, 'officevehicle')
router.register(r'airportfurniture', AirportFurnitureApi, 'airportfurniture')
router.register(r'banner', BannerApi, 'banner')
router.register(r'officefurniture', OfficeFurnitureApi, 'officefurniture')
router.register(r'digitalfurniture', DigitalFurnitureApi, 'digitalfurniture')
router.register(r'checksproduct', ChecksProductApi, 'checksproduct')
router.register(r'transmission', TransmissionApi, 'transmission')
router.register(r'autoincrementproductcheck', AutoIncrementProductCheckApi, 'autoincrementproductcheck')
router.register(r'consumable-list', ConsumableApi, 'consumable-list')
router.register(r'autoincrementproduct', AutoIncrementProductApi, 'autoincrementproduct')
router.register(r'autoincrementproductfactor', AutoIncrementProductFactorApi, 'autoincrementproductfactor')
router.register(r'factorsproduct', FactorsProductApi, 'factorsproduct')
router.register(r'category-list', CategoryApi, 'category-list')
router.register(r'benefit', BenefitApi, 'benefit')
router.register(r'facilityfurniture', FacilityFurnitureApi, 'facilityfurniture')
router.register(r'factors', FactorsApi, 'factors')
router.register(r'electronicfurniture', ElectronicFurnitureApi, 'electronicfurniture')
router.register(r'supportitem', SupportItemApi, 'supportitem')
router.register(r'industrialtool', IndustrialToolApi, 'industrialtool')
router.register(r'maintenance', MaintenanceApi, 'maintenance')
router.register(r'noneindustrialtool', NoneIndustrialToolApi, 'noneindustrialtool')
router.register(r'autoincrementfactorproperty', AutoIncrementFactorPropertyApi, 'autoincrementfactorproperty')
router.register(r'repairedigitalfurniture', RepairedDigitalFurnitureApi, 'repairedigitalfurniture')
router.register(r'repairedfacilityfurniture', RepairedFacilityFurnitureApi, 'repairedfacilityfurniture')
router.register(r'repairedofficefurniture', RepairedOfficeFurnitureApi, 'repairedofficefurniture')
router.register(r'repairedairplane', RepairedAirplaneApi, 'repairedairplane')
router.register(r'repairedairportfurniture', RepairedAirportFurnitureApi, 'repairedairportfurniture')
router.register(r'repairedelectronicfurniture', RepairedElectronicFurnitureApi, 'repairedelectronicfurniture')
router.register(r'repairedsafetyequipment', RepairedSafetyEquipmentApi, 'repairedsafetyequipment')
router.register(r'repairedairportequipment', RepairedAirportEquipmentApi, 'repairedairportequipment')
router.register(r'repairedairportvehicle', RepairedAirportVehicleApi, 'repairedairportvehicle')
router.register(r'repairedofficevehicle', RepairedOfficeVehicleApi, 'repairedofficevehicle')
router.register(r'repairedindustrialtool', RepairedIndustrialToolApi, 'repairedindustrialtool')
router.register(r'handling-product', HandlingApi, 'handling-product')


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
