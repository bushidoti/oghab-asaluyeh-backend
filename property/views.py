import django_filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from .models import *


class AutoIncrementPropertyApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AutoIncrementSerializer
    queryset = AutoIncrementProperty.objects.all()


class AirportEquipmentApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AirportEquipmentSerializer
    queryset = AirportEquipment.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'install_location', 'model', 'year_made', 'owner']


class SafetyEquipmentApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = SafetyEquipmentSerializer
    queryset = SafetyEquipment.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'install_location', 'use_for']


class AirportVehicleApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AirportVehicleSerializer
    queryset = AirportVehicle.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'year_made', 'model', 'chassis', 'motor', 'plate1', 'plate2', 'plate3',
                        'plate4', 'owner']


class AirplaneApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AirplaneSerializer
    queryset = Airplane.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'year_made', 'model', 'chassis', 'motor', 'plate1', 'plate2', 'plate3',
                        'plate4', 'owner']


class OfficeVehicleApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = OfficeVehicleSerializer
    queryset = OfficeVehicle.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'year_made', 'model', 'chassis', 'motor', 'plate1', 'plate2', 'plate3',
                        'plate4', 'owner']


class AirportFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AirportFurnitureSerializer
    queryset = AirportFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location']


class FacilityFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = FacilityFurnitureSerializer
    queryset = FacilityFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location', 'model', 'user']


class DigitalFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = DigitalFurnitureSerializer
    queryset = DigitalFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'install_location', 'model', 'user']


class OfficeFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = OfficeFurnitureSerializer
    queryset = OfficeFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'using_location', 'user', 'year_made']


class ElectronicFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = ElectronicFurnitureSerializer
    queryset = ElectronicFurniture.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'install_location', 'model', 'year_buy', 'user']


class NoneIndustrialToolApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = NoneIndustrialToolSerializer
    queryset = NoneIndustrialTool.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'user', 'using_location']


class IndustrialToolApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = IndustrialToolSerializer
    queryset = IndustrialTool.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'year_buy', 'user', 'using_location', 'model']


class BenefitApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = BenefitSerializer
    queryset = Benefit.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'number_type', 'number', 'using_location']


class SupportItemApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = SupportItemSerializer
    queryset = SupportItem.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'user', 'using_location', 'model', 'type_item']


class FactorsApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = FactorsSerializer
    queryset = Factors.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'date', 'document_code', 'systemID','inventory']


class RepairedDigitalFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedDigitalFurnitureSerializer
    queryset = RepairedDigitalFurniture.objects.all()


class RepairedFacilityFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedFacilityFurnitureSerializer
    queryset = RepairedFacilityFurniture.objects.all()


class RepairedOfficeFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedOfficeFurnitureSerializer
    queryset = RepairedOfficeFurniture.objects.all()


class RepairedAirportFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedAirportFurnitureSerializer
    queryset = RepairedAirportFurniture.objects.all()


class RepairedElectronicFurnitureApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedElectronicFurnitureSerializer
    queryset = RepairedElectronicFurniture.objects.all()


class RepairedSafetyEquipmentApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedSafetyEquipmentSerializer
    queryset = RepairedSafetyEquipment.objects.all()


class RepairedAirportEquipmentApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedAirportEquipmentSerializer
    queryset = RepairedAirportEquipment.objects.all()


class RepairedAirportVehicleApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedAirportVehicleSerializer
    queryset = RepairedAirportVehicle.objects.all()


class RepairedAirplaneApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedAirplaneSerializer
    queryset = RepairedAirplane.objects.all()


class RepairedOfficeVehicleApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedOfficeVehicleSerializer
    queryset = RepairedOfficeVehicle.objects.all()


class RepairedIndustrialToolApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = RepairedIndustrialToolSerializer
    queryset = RepairedIndustrialTool.objects.all()


class AutoIncrementFactorPropertyApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AutoIncrementFactorSerializer
    queryset = AutoIncrementFactor.objects.all()
