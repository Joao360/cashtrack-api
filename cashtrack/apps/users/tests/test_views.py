from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from ..models import User
from ..serializers import UserSerializer


factory = APIRequestFactory()


class AuthTest(APITestCase):
    """ Test module for AUTH """

    def setUp(self):
        user = User.objects.create(email="test@mail.com")
        user.set_password("Test123!")
        user.save()

        self.valid_payload = {"username": "test@mail.com", "password": "Test123!"}
        self.invalid_payload = {"username": "test@mail.com", "password": "Test1234!"}

    def test_successful_sign_in(self):
        response = self.client.post(
            reverse("sign-in"), self.valid_payload, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "token")
        self.assertContains(response, "token_expires_in")

    def test_unsuccessful_sign_in(self):
        response = self.client.post(
            reverse("sign-in"), self.invalid_payload, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserTest(APITestCase):
    def setUp(self):
        self.test = User.objects.create(email="test@mail.com")
        self.test.set_password("Test123!")
        self.test.save()

        self.another_test = User.objects.create(email="another_test@mail.com")
        self.another_test.set_password("Test123!")
        self.another_test.save()

        self.client.force_authenticate(user=self.test)

        self.update_body = {
            "email": "test@mail.com",
            "password": "Test123!",
            "first_name": "João",
            "last_name": "Graça",
        }

    # It will retrieve the database object and prepare both objects to be compared by assertEqual
    def prepare_data_for_comparison(self, response, request):
        test = User.objects.get(pk=self.test.pk)
        serializer = UserSerializer(test, context={"request": request})
        data = serializer.data

        # Remove expiration date since it will always be different
        response.data.pop("token_expires_in")
        data.pop("token_expires_in")

        return data

    def test_get_own_details(self):
        request = factory.get(reverse("user-detail", kwargs={"pk": self.test.pk}))
        force_authenticate(request, user=self.test)

        response = self.client.get(reverse("user-detail", kwargs={"pk": self.test.pk}))

        data = self.prepare_data_for_comparison(response, request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_get_other_details(self):
        response = self.client.get(
            reverse("user-detail", kwargs={"pk": self.another_test.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_self(self):
        request = factory.put(
            reverse("user-detail", kwargs={"pk": self.test.pk}),
            self.update_body,
            format="json",
        )
        force_authenticate(request, user=self.test)

        response = self.client.put(
            reverse("user-detail", kwargs={"pk": self.test.pk}),
            self.update_body,
            format="json",
        )

        data = self.prepare_data_for_comparison(response, request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_update_other(self):
        response = self.client.put(
            reverse("user-detail", kwargs={"pk": self.another_test.pk}),
            self.update_body,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_self(self):
        response = self.client.delete(
            reverse("user-detail", kwargs={"pk": self.test.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(pk=self.test.pk).exists(), False)

    def test_delete_other(self):
        response = self.client.delete(
            reverse("user-detail", kwargs={"pk": self.another_test.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.filter(pk=self.another_test.pk).exists(), True)
