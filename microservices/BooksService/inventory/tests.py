from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class InventoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_books(self):
        response = self.client.get('/inventory/getbooks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_add_book(self):
        data = {'title': 'Updated Book Title','author':'test author','isbn':1235,'stock':10}
        response = self.client.post('/inventory/addbook', data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_update_book(self):
        data = {'title': 'Updated Book Title','author':'test author','isbn':453,'stock':100}
        response = self.client.patch('/inventory/updatebook/1', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       

    def test_delete_book(self):
        response = self.client.delete('/inventory/deletebook/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     

