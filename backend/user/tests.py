from rest_framework.test import APITestCase
from rest_framework import status

class UserAPITest(APITestCase):
    def test_create_user(self):
        data = {
            "bob",
            "bobby",
            "habib",
            "bob@habib.com"
            "1234"
        }

        response = self.client.post(
            "/user/register/",
            data,
            format="json"
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data["name"],
            "John"
        )

    def test_login_user(self):
        data = {
            "bob@habib.com"
            "1234"
        }

        response = self.client.post("/user/login/")

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

