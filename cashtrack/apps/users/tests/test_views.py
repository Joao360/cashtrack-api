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

    def test_get_own_details(self):
        self.client.force_authenticate(user=self.test)
        request = factory.get(reverse("user-detail", kwargs={"pk": self.test.pk}))
        force_authenticate(request, user=self.test)

        response = self.client.get(reverse("user-detail", kwargs={"pk": self.test.pk}))

        test = User.objects.get(pk=self.test.pk)
        serializer = UserSerializer(test, context={"request": request})
        data = serializer.data

        # Remove expiration date since it will always be different
        response.data.pop("token_expires_in")
        data.pop("token_expires_in")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_get_other_details(self):
        self.client.force_authenticate(user=self.another_test)

        response = self.client.get(reverse("user-detail", kwargs={"pk": self.test.pk}))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
