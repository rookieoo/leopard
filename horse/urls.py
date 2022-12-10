from django.urls import include, path
from rest_framework import routers

from horse.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')

app_name = 'horse'
urlpatterns = [
    path('', include(router.urls)),
]
