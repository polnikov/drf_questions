from api import views

from django.urls import include, path

from rest_framework import routers


app_name = 'api'

router = routers.SimpleRouter()
router.register('entity', views.EntityViewSet)
router.register('property', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
