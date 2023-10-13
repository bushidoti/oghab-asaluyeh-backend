from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class AllProductsSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = AllProducts
        fields = '__all__'
        extra_fields = ['inventory', 'category']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(AllProductsSerializer, self).get_field_names(
            declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = ['value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['value']


class HandlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handling
        fields = '__all__'


class AutoIncrementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrement
        fields = '__all__'


class AutoIncrementProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementProduct
        fields = '__all__'


class AutoIncrementProductFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementProductFactor
        fields = '__all__'


class AutoIncrementProductCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementProductCheck
        fields = '__all__'


class AutoIncrementCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementCheck
        fields = '__all__'


class AutoIncrementFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoIncrementFactor
        fields = '__all__'


class FactorsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorsProduct
        fields = '__all__'


class ChecksProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCheck
        fields = '__all__'
