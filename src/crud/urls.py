from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crud.views import diagnosis
from crud.views import file

app_name='crud'
router = DefaultRouter()
router.register('diagnoses', diagnosis.DiagnosisModelViewSet, basename='diagnoses')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', file.UploadFileAPIView.as_view(), name='upload-file'),
]