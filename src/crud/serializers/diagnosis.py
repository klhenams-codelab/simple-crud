from rest_framework import serializers

from crud.models import Diagnosis


class DiagnosisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiagnosisWithFullCodeModelSerializer(DiagnosisModelSerializer):
    full_code = serializers.CharField(required=False, source='get_full_code')