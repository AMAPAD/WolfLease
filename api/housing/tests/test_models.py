from django.test import TestCase
from housing.models import (Apartment, Flat, User, Interested)
                            # ,TenantsRights)

class InterestedModelTests(TestCase):
    def setUp(self):  # setUp method to initialize data before each test method is executed.
        self.apartment = Apartment.objects.create(address="Test Address")  # Creates an Apartment instance for use in tests.
        self.flat = Flat.objects.create(availability=True, associated_apt_id=self.apartment, floor_number=2, rent_per_room=500)  # Creates a Flat instance related to the apartment.
        self.user = User.objects.create(contact_number="1234567890", dob="2000-01-01")  # Creates a User instance.

    def test_create_interested(self):  # Defines a test method to check the creation of Interested instances.
        interested = Interested.objects.create(apartment_id=self.apartment, flat_id=self.flat, user_id=self.user)  # Creates an Interested instance.
        self.assertEqual(Interested.objects.count(), 1)  # Asserts that there is exactly one Interested record in the database.

    def test_cascade_delete_on_flat(self):  # Tests the cascade delete behavior when a Flat is deleted.
        interested = Interested.objects.create(apartment_id=self.apartment, flat_id=self.flat, user_id=self.user)  # Creates an Interested instance.
        self.flat.delete()  # Deletes the Flat instance.
        self.assertEqual(Interested.objects.count(), 0)  # Asserts that there are no Interested records left after the Flat is deleted.

    def test_do_nothing_delete_on_apartment(self):  # Tests the behavior when an Apartment is deleted.
        interested = Interested.objects.create(apartment_id=self.apartment, flat_id=self.flat, user_id=self.user)  # Creates an Interested instance.
        self.apartment.delete()  # Deletes the Apartment instance.
        self.assertEqual(Interested.objects.count(), 0)  # Asserts that the Interested record does not exists after the Apartment is deleted.