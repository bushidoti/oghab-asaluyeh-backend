import django_filters
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from .serializer import PersonSerializer, PropertySerializer
from .models import Person, Property
from rest_framework.permissions import BasePermission
from django_filters.fields import CSVWidget, MultipleChoiceField
from django_filters import rest_framework as df_filters


class MyPermission(BasePermission):
    message = "دسترسی لازم را ندارید."
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


class MultipleField(MultipleChoiceField):
    def valid_value(self, value):
        return True


class MultipleFilter(df_filters.MultipleChoiceFilter):
    field_class = MultipleField


class PersonFilter(django_filters.rest_framework.FilterSet):
    full_name = django_filters.rest_framework.CharFilter(field_name='full_name', lookup_expr='contains')
    sex = MultipleFilter(
        lookup_expr="contains",
        field_name="sex",
        widget=CSVWidget
    )
    type = django_filters.rest_framework.CharFilter(field_name='type', lookup_expr='contains')
    national_id = django_filters.rest_framework.CharFilter(field_name='national_id', lookup_expr='contains')
    job = django_filters.rest_framework.CharFilter(field_name='job', lookup_expr='contains')
    office = MultipleFilter(
        lookup_expr="contains",
        field_name="office",
        widget=CSVWidget
    )
    date = django_filters.rest_framework.CharFilter(field_name='date', lookup_expr='contains')
    id = django_filters.rest_framework.NumberFilter(field_name='id', lookup_expr='contains')
    clearedStatus = django_filters.rest_framework.BooleanFilter(field_name='clearedStatus', lookup_expr='contains')

    class Meta:
        model = Person
        fields = ['full_name', 'sex', 'type', 'national_id', 'office', 'job',
                  'date', 'clearedStatus', 'id']


class PersonApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "propertyManagement.person"

    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PersonFilter


class PropertyApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "propertyManagement.property"

    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'docNumber', 'landlord', 'madeOf', 'plateMotor', 'id',
                        'typeProperty', 'part1plate', 'part2plate', 'part3plate', 'cityPlate', 'addressChassis',
                        'modelMeter', 'descriptionLocation', 'soldStatus']
