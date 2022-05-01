from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from crud.models import Diagnosis


class DiagnosisTests(APITestCase):

    def setUp(self):
        self.data = {
            "category_code": "A00",
            "category_title": "Cholera",
            "diagnosis_code": "0",
            "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
        }
        self.response = self.client.post(
            reverse('crud:diagnoses-list'),
            self.data,
            format="json")

    def test_api_create_diagnosis(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Diagnosis.objects.count(), 1)
        self.assertEqual(Diagnosis.objects.get().category_code, 'A00')

    def test_api_list_diagnoses(self):
        url = reverse('crud:diagnoses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Diagnosis.objects.count(), 1)

    def test_api_can_get_a_diagnosis(self):
        diagnosis = Diagnosis.objects.get()
        response = self.client.get(
            reverse('crud:diagnoses-detail',
                    kwargs={'pk': diagnosis.id}), format="json"
        )
        self.assertContains(response, diagnosis.full_description)

    def test_api_can_update_a_diagnosis(self):
        diagnosis = Diagnosis.objects.get()
        new_data = {
            "category_code": "A00",
            "category_title": "Cholera",
            "diagnosis_code": 1,
            "abbreviated_description": "Cholera due to Vibrio cholerae 01, biovar eltor",
            "full_description": "Cholera due to Vibrio cholerae 01, biovar eltor",
        }
        response = self.client.put(
            reverse('crud:diagnoses-detail',
                    kwargs={'pk': diagnosis.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Diagnosis.objects.get().full_description,
                         'Cholera due to Vibrio cholerae 01, biovar eltor')

    def test_api_can_delete_a_diagnosis(self):
        diagnosis = Diagnosis.objects.get()
        response = self.client.delete(
            reverse('crud:diagnoses-detail',
                    kwargs={'pk': diagnosis.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Diagnosis.objects.count(), 0)
