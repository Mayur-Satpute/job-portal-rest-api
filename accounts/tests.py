
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class RegistrationTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/auth/register/"

    def test_candidate_registration_success(self):
        payload = {
            "username": "candidate_new",
            "email": "candidate_new@example.com",
            "password": "SecurePass123!",
            "first_name": "Test",
            "last_name": "Candidate",
            "role": "CANDIDATE",
        }

        response = self.client.post(
            self.register_url, payload, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", response.data)

        user = User.objects.get(username="candidate_new")
        self.assertTrue(user.check_password("SecurePass123!"))

    def test_admin_role_registration_rejected(self):
        payload = {
            "username": "fake_admin",
            "email": "fake_admin@example.com",
            "password": "SecurePass123!",
            "role": "ADMIN",
        }

        response = self.client.post(
            self.register_url, payload, format="json"
        )

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertFalse(User.objects.filter(username="fake_admin").exists())

    def test_duplicate_email_rejected(self):
        User.objects.create_user(
            username="existing_user",
            email="duplicate@example.com",
            password="SecurePass123!",
        )

        payload = {
            "username": "another_user",
            "email": "duplicate@example.com",
            "password": "SecurePass123!",
            "role": "CANDIDATE",
        }

        response = self.client.post(
            self.register_url, payload, format="json"
        )

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="auth_candidate",
            email="auth_candidate@example.com",
            password="SecurePass123!",
            role=User.Role.CANDIDATE,
        )
        self.me_url = "/api/auth/me/"

    def test_me_rejects_unauthenticated_request(self):
        response = self.client.get(self.me_url)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_me_accepts_valid_jwt(self):
        access_token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.get(self.me_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "auth_candidate")
        self.assertEqual(response.data["role"], "CANDIDATE")
