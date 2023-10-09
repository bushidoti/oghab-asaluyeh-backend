from .serializer import ProductSerializer, AllProductsSerializer, AutoIncrementSerializer, HandlingSerializer, \
    AutoIncrementCheckSerializer, AutoIncrementFactorSerializer
from .models import Product, AllProducts, AutoIncrement, Handling, AutoIncrementCheck, AutoIncrementFactor
import django_filters
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
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


class ProductFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.rest_framework.CharFilter(field_name='name', lookup_expr='contains')
    type = django_filters.rest_framework.CharFilter(field_name='type', lookup_expr='contains')
    inventory = MultipleFilter(
        lookup_expr="contains",
        field_name="inventory",
        widget=CSVWidget
    )
    code = django_filters.rest_framework.NumberFilter(field_name='code', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['code', 'name', 'category','inventory']


class ProductApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "warhouse.product"

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter


class AllProductstApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AllProductsSerializer
    queryset = AllProducts.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'date', 'consumable', 'document_code', 'document_type', 'operator', 'receiver', 'buyer',
                        'systemID',
                        'name', 'product']


class AutoIncrementApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AutoIncrementSerializer
    queryset = AutoIncrement.objects.all()


class AutoIncrementCheckApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AutoIncrementCheckSerializer
    queryset = AutoIncrementCheck.objects.all()


class AutoIncrementFactorApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AutoIncrementFactorSerializer
    queryset = AutoIncrementFactor.objects.all()


class HandlingApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = HandlingSerializer
    queryset = Handling.objects.all()
