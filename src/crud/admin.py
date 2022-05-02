from django.contrib import admin

from crud.models import Diagnosis

@admin.register(Diagnosis)
class TrackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Diagnosis._meta.get_fields() if field.name != 'id']