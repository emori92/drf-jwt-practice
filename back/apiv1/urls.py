from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views


# router
router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
