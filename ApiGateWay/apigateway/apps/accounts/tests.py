# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.contrib.auth.models import User

# class TestAuthenticationViews(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user_data = {
#             'username': 'test_user',
#             'password': 'test_password'
#         }
#         self.invalid_user_data = {
#             'username': 'non_existing_user',
#             'password': 'invalid_password'
#         }
#         self.registration_data = {
#             'username': 'new_user',
#             'password': 'new_password'
#         }
#         User.objects.create_user(username='existing_user', password='existing_password')

#     def test_valid_user_login(self):
#         response = self.client.post('/login', data=self.user_data)
#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.assertTrue('access' in response.data)
#         self.assertTrue('refresh' in response.data)

#     def test_invalid_user_login_user_not_exist(self):
#         response = self.client.post('/login', data=self.invalid_user_data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertEqual(response.data['reason'], 'User does not exist.')

#     def test_invalid_user_login_incorrect_password(self):
#         invalid_password_data = self.user_data.copy()
#         invalid_password_data['password'] = 'incorrect_password'
#         response = self.client.post('/login', data=invalid_password_data)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertEqual(response.data['reason'], 'invalid credentials')

#     def test_missing_username_or_password_login(self):
#         invalid_data = {}
#         response = self.client.post('/login', data=invalid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data['reason'], 'Invalid message or body!')

#     def test_valid_user_registration(self):
#         response = self.client.post('/register', data=self.registration_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['result'], 'user created successfully.')

   
 