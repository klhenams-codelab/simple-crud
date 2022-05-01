from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crud import views

app_name='crud'
router = DefaultRouter()
router.register('diagnoses', views.DiagnosisModelViewSet, basename='diagnoses')

urlpatterns = [
    path('', include(router.urls)),
]