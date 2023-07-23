import django_filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import ProductSerializer, AllProductsSerializer, AutoIncrementSerializer, HandlingSerializer, \
    AutoIncrementCheckSerializer, AutoIncrementFactorSerializer
from .models import Product, AllProducts, AutoIncrement, Handling, AutoIncrementCheck, AutoIncrementFactor


class ProductApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['code', 'name', 'category', 'date',
                        'inventory', 'recycle_status', 'operator']


class AllProductstApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = AllProductsSerializer
    queryset = AllProducts.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'date', 'consumable', 'document_code', 'document_type', 'operator', 'receiver', 'buyer', 'systemID',
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
