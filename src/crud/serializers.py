from rest_framework import serializers

from crud.models import Diagnosis


class DiagnosisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'