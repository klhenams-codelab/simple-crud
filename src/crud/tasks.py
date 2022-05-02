from celery import shared_task

from crud.utils.importer import csv_to_db
from crud.models import DiagnosisFile

@shared_task
def csv_to_db_task(diagnosis_file: int):
    try:
        obj = DiagnosisFile.objects.get(pk=diagnosis_file)
        csv_to_db(obj.file.path)
    except Exception as err:
        pass