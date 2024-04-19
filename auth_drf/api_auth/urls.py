from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_data_viewset

router = DefaultRouter
router.register(r'user-data', user_data_viewset)