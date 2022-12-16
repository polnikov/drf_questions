from api.models import Entity, Property
from api import serializers
from rest_framework import viewsets, permissions


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = serializers.EntitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = serializers.PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
