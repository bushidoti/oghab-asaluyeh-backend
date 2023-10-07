import django_filters
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from .serializer import PersonSerializer, PropertySerializer
from .models import Person, Property
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = "You do not have permission to perform action"
    permission_map = {
        "GET": "{app_label}.view_{model_name}",
        "POST": "{app_label}.add_{model_name}",
        "PUT": "{app_label}.change_{model_name}",
        "PATCH": "{app_label}.change_{model_name}",
        "DELETE": "{app_label}.delete_{model_name}",
    }

    def _get_permission(self, method, perm_slug):
        app, model = perm_slug.split(".")
        if method not in self.permission_map:
            raise MethodNotAllowed(method)
        perm = self.permission_map.get(method).format(app_label=app, model_name=model)
        return perm

    def has_permission(self, request, view):
        perm = self._get_permission(
            method=request.method, perm_slug=view.perm_slug
        )
        if request.user.has_perm(perm):
            return True
        return False


class PersonApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "propertyManagement.person"

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['full_name', 'sex', 'type', 'national_id', 'office', 'job',
                        'date', 'clearedStatus', 'id']


class PropertyApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "propertyManagement.property"

    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'docNumber', 'landlord', 'madeOf', 'plateMotor', 'id',
                        'typeProperty', 'part1plate', 'part2plate', 'part3plate', 'cityPlate', 'addressChassis',
                        'modelMeter', 'descriptionLocation', 'soldStatus']
