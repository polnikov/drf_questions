from django.contrib import admin
from api.models import Entity, Property


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'modified_by', 'value', 'get_properties')
    ordering = ['id']

    def get_properties(self, obj):
        return [prop.key for prop in obj.properties.all()]
    get_properties.short_description = 'properties'


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')
    ordering = ['id']
