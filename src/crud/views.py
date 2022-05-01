from rest_framework import viewsets
from rest_framework import permissions


from crud.models import Diagnosis
from crud.serializers import DiagnosisModelSerializer




class DiagnosisModelViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisModelSerializer
    permission_classes = [permissions.AllowAny]