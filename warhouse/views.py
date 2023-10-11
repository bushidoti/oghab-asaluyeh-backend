from rest_framework.response import Response

from .serializer import *
from .models import *
import django_filters
from rest_framework import viewsets, status
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
    name_exact = django_filters.rest_framework.CharFilter(field_name='name', lookup_expr='exact')
    inventory = MultipleFilter(
        lookup_expr="contains",
        field_name="inventory",
        widget=CSVWidget
    )
    category = MultipleFilter(
        lookup_expr="contains",
        field_name="category",
        widget=CSVWidget
    )
    code = django_filters.rest_framework.NumberFilter(field_name='code', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['code', 'name', 'category', 'inventory', 'name_exact']


class ProductApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "warhouse.product"

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter


class AllProductstFilter(django_filters.rest_framework.FilterSet):
    date = django_filters.rest_framework.CharFilter(field_name='date', lookup_expr='contains')
    scale = django_filters.rest_framework.CharFilter(field_name='scale', lookup_expr='contains')
    buyer = django_filters.rest_framework.CharFilter(field_name='buyer', lookup_expr='contains')
    name = django_filters.rest_framework.CharFilter(field_name='name', lookup_expr='contains')
    amendment = django_filters.rest_framework.CharFilter(field_name='amendment', lookup_expr='contains')
    receiver = django_filters.rest_framework.CharFilter(field_name='receiver', lookup_expr='contains')
    seller = django_filters.rest_framework.CharFilter(field_name='seller', lookup_expr='contains')
    document_code = django_filters.rest_framework.CharFilter(field_name='document_code', lookup_expr='contains')
    document_type = django_filters.rest_framework.CharFilter(field_name='document_type', lookup_expr='contains')
    id = django_filters.rest_framework.CharFilter(field_name='id', lookup_expr='exact')
    systemID = django_filters.rest_framework.CharFilter(field_name='systemID', lookup_expr='exact')
    operator = MultipleFilter(
        lookup_expr="contains",
        field_name="operator",
        widget=CSVWidget
    )
    consumable = MultipleFilter(
        lookup_expr="contains",
        field_name="consumable",
        widget=CSVWidget
    )
    product = django_filters.rest_framework.NumberFilter(field_name='product', lookup_expr='exact')

    class Meta:
        model = AllProducts
        fields = ['id', 'date', 'seller', 'amendment', 'consumable', 'scale', 'document_code', 'document_type',
                  'operator', 'receiver',
                  'buyer',
                  'systemID',
                  'name', 'product']


class AllProductstApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "warhouse.allproducts"

    serializer_class = AllProductsSerializer
    queryset = AllProducts.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = AllProductstFilter

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(AllProductstApi, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ConsumableApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "warhouse.allproducts"

    serializer_class = ConsumableSerializer
    queryset = Consumable.objects.all()


class CategoryApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "warhouse.allproducts"

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


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
