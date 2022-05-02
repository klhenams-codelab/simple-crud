from rest_framework import serializers

from crud.models import DiagnosisFile



class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisFile
        fields = '__all__'