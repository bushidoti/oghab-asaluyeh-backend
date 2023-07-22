import django_filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import PersonSerializer, PropertySerializer
from .models import Person, Property


class PersonApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['full_name', 'sex', 'type', 'national_id', 'office', 'job',
                        'date', 'clearedStatus', 'id']


class PropertyApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'docNumber', 'landlord', 'madeOf', 'plateMotor', 'id',
                        'typeProperty', 'part1plate', 'part2plate', 'part3plate', 'cityPlate', 'addressChassis',
                        'modelMeter', 'descriptionLocation', 'soldStatus']
