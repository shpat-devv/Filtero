from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class UserAPITest(APITestCase):
    register_url = "/user/register/"
    login_url = "/user/login/"
    edit_url = "/user/edit/"

    def setUp(self):
        """
        Runs before every test.

        Create a user that can be used by tests that require
        an existing account.
        """
        self.user_data = {
            "username": "bob",
            "first_name": "Bobby",
            "last_name": "Habib",
            "email": "bob@habib.com",
            "password": "1234",
        }

        self.user = User.objects.create_user(
            username=self.user_data["username"],
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            email=self.user_data["email"],
            password=self.user_data["password"],
        )

    def login(self):
        """
        Log in through the API and return the JWT tokens.
        """
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        return response.data["access"], response.data["refresh"]

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def test_create_user(self):
        """
        A new user should be successfully registered.
        """
        data = {
            "username": "alice",
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
            "password": "secure-password-123",
        }

        response = self.client.post(
            self.register_url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            User.objects.filter(email="alice@example.com").exists()
        )

    def test_create_user_with_duplicate_email(self):
        """
        Registering another user with an existing email should fail.
        """
        data = {
            "username": "anotherbob",
            "first_name": "Another",
            "last_name": "Bob",
            "email": self.user_data["email"],
            "password": "secure-password-123",
        }

        response = self.client.post(
            self.register_url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    def test_create_user_with_missing_password(self):
        """
        Registration should fail if the password is missing.
        """
        data = {
            "username": "alice",
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
        }

        response = self.client.post(
            self.register_url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    # ---------------------------------------------------------
    # Login
    # ---------------------------------------------------------

    def test_login_user(self):
        """
        A user with valid credentials should receive JWT tokens.
        """
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"],
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

        self.assertTrue(response.data["access"])
        self.assertTrue(response.data["refresh"])

    def test_login_with_wrong_password(self):
        """
        Login should fail with an incorrect password.
        """
        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": "wrong-password",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_login_with_nonexistent_user(self):
        """
        Login should fail for an account that does not exist.
        """
        response = self.client.post(
            self.login_url,
            {
                "email": "doesnotexist@example.com",
                "password": "some-password",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    # ---------------------------------------------------------
    # Authentication
    # ---------------------------------------------------------

    def test_authenticated_request(self):
        """
        Verify that a valid JWT access token authenticates the user.
        """
        access_token, _ = self.login()

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.get(self.edit_url)

        self.assertNotEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_unauthenticated_edit_user(self):
        """
        Editing a user without authentication should fail.
        """
        response = self.client.patch(
            self.edit_url,
            {
                "first_name": "Updated",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    # ---------------------------------------------------------
    # Edit user
    # ---------------------------------------------------------

    def test_edit_user(self):
        """
        An authenticated user should be able to edit their profile.
        """
        access_token, _ = self.login()

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        data = {
            "first_name": "Updated",
            "last_name": "User",
        }

        response = self.client.patch(
            self.edit_url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.first_name,
            "Updated",
        )

        self.assertEqual(
            self.user.last_name,
            "User",
        )

    def test_edit_user_email(self):
        """
        An authenticated user should be able to update their email,
        assuming your API allows email updates.
        """
        access_token, _ = self.login()

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.patch(
            self.edit_url,
            {
                "email": "newemail@example.com",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.email,
            "newemail@example.com",
        )
