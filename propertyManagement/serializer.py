from rest_framework import serializers
from .models import Immovable, Person , Movable


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


class MovableSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Movable
        fields = '__all__'


class ImmovableSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Immovable
        fields = '__all__'


class PersonSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
