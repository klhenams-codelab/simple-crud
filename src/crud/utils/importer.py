import csv
from crud.models import Diagnosis
from rest_framework.exceptions import APIException


def csv_to_db(file_path: str):

    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        diagnosis_code_list = list(reader)
        objs = [
            Diagnosis(
                category_code=diagnosis_code[0],
                diagnosis_code=diagnosis_code[1],
                abbreviated_description=diagnosis_code[3],
                full_description=diagnosis_code[4],
                category_title=diagnosis_code[5]
            )
            for diagnosis_code in diagnosis_code_list
        ]

    # print(objs)
    try:
        Diagnosis.objects.bulk_create(objs, ignore_conflicts=True)
    except Exception as err:
        # Pass to logger or something
        raise APIException(f'Error: {err}')
