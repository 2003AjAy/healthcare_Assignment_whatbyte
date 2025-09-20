# core/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet, MappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('', include(router.urls)),
]
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView