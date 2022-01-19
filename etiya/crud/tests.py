from django.test import TestCase
from rest_framework.test import APITestCase
# Create your tests here.
from django.urls import reverse
import json


class apitest(APITestCase):
    def createTest(self):
        url = reverse("crud_create")
        data = {"text": "test", "label": "test"}
        response = self.client.post(url,data, format='json')
        self.assertEqual(response.status_code, 201)

    def listTest(self):
        url = reverse("crud_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def deleteTest(self):
        url = reverse("delete_crud", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def updateTest(self):
        url = reverse("update_crud", kwargs={"pk": 1})
        data = {"text": "test", "label": "test"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
