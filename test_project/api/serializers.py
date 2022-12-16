from rest_framework import serializers
from api.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = Property
        fields = ('key', 'value')


class EntitySerializer(serializers.ModelSerializer):
    modified_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    value = serializers.IntegerField()
    properties = PropertySerializer(read_only=True, many=True)

    class Meta:
        model = Entity
        fields = ('id', 'modified_by', 'value', 'properties')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['properties'] = {i['key']: i['value'] for i in res['properties']}
        return res
