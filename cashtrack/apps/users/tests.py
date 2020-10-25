from django.test import TestCase

from .models import User

# Create your tests here.
class UserTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(
            email="Casper@mail.com", first_name="Casper", last_name="Felix"
        )
        User.objects.create(
            email="Victor@mail.com", first_name="Victor", last_name="Felix"
        )

    def test_user_model(self):
        casper = User.objects.get(email="Casper@mail.com")
        victor = User.objects.get(email="Victor@mail.com")
        self.assertEqual(casper.first_name, "Casper")
        self.assertEqual(victor.first_name, "Victor")
