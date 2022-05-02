from django.db import models


class Diagnosis(models.Model):
    category_code = models.CharField(max_length=10)
    diagnosis_code = models.CharField(max_length=5, blank=True, null=True)
    category_title = models.CharField(max_length=255)
    abbreviated_description = models.CharField(max_length=255)
    full_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category_code}{self.diagnosis_code}'

    def get_full_code(self):
        return self.__str__()

    class Meta:
        unique_together = ('category_code', 'diagnosis_code')
        ordering = ("-created_at",)
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'


class DiagnosisFile(models.Model):
    file = models.FileField(upload_to='diagnosis')
    upload_at = models.DateTimeField(auto_now=True)
