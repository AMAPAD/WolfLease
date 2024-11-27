import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from api.housing.models import (Apartment, Flat, User, Interested)
from datetime import date

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def setup_test_data(db):
    # Create test data
  
    
    # lease = Lease.objects.create(
    #     lease_start_date='2022-10-05',
    #     lease_end_date='2026-10-04'
    # )
    
    apartment = Apartment.objects.create(
        address="Stovall Dr"
    )
    
    flat = Flat.objects.create(
        availability=True,
        associated_apt_id=apartment,
        #lease_id=lease,
        floor_number=3,
        rent_per_room=450
    )
    
    user = User.objects.create(
        flat_id=flat,
        contact_number='7876756487',
        dob='2000-10-07'
    )
    
    interested = Interested.objects.create(
        user_id=user,
        flat_id=flat,
        apartment_id=apartment
    )
    
    return {
        #'owner': owner,
        #'lease': lease,
        'apartment': apartment,
        'flat': flat,
        'user': user,
        'interested': interested
    }

@pytest.fixture
def apartment_data():
    return {
        'address': 'ClarionHeights',
        'facilities': 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym'
    }

# Owner Tests
# def test_create_owner(api_client):
#     url = '/owners'
#     data = {
#         'contact_number': '1234567890',
#         'contact_email': 'test@testing.com',
#         'password': 'test'
#     }
#     response = api_client.post(url, data, format='json')
#     assert response.status_code == 201
#     assert Owner.objects.count() == 1
#     assert Owner.objects.get().contact_email == 'test@testing.com'

# Flat Tests
def test_create_flat(api_client, setup_test_data):
    url = '/flats'
    data = {
        'availability': True,
        'associated_apt_id': str(setup_test_data['apartment'].id),
        #'lease_id': str(setup_test_data['lease'].id),
        'floor_number': 1,
        'rent_per_room': 540
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Flat.objects.count() == 2  # One from setup + one new
    assert str(Flat.objects.filter(availability=True).first().availability) == 'True'

# Apartment Tests
def test_create_apartment(api_client, setup_test_data):
    url = '/api/apartments/'  # Most Django REST APIs include '/api/' prefix
    data = {
        'address': '1130 Clarion Heights Ln, Crab Orchard Drive, Raleigh NC 27606',
        'facilities': 'Washer, Dryer, Oven, Swimming Pool, Club House, Gym',
        #'owner_id': str(setup_test_data['owner'].id)
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Apartment.objects.count() == 2  # One from setup + one new

# User Tests
def test_create_user(api_client, setup_test_data):
    url = '/users'
    data = {
        'flat_id': str(setup_test_data['flat'].id),
        'contact_number': '8454210259',
        'contact_email': 'test@test.com',
        'password': 'password',
        'dob': '2000-10-10'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert User.objects.count() == 2  # One from setup + one new

# Lease Tests
# def test_create_lease(api_client):
#     url = '/lease'
#     data = {
#         'lease_start_date': '2022-10-05',
#         'lease_end_date': '2026-10-04'
#     }
#     response = api_client.post(url, data, format='json')
#     assert response.status_code == 201
#     assert Lease.objects.count() == 1

# Search Tests
@pytest.mark.django_db
def test_search_apartment(api_client, apartment_data):
    # Create test apartment
    url = reverse('apartment-list')  # Use URL name from urls.py
    apartment = api_client.post(url, apartment_data).json()
    
    # Test search
    response = api_client.get(
        url,
        {'search': 'ClarionHeights'},
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['facilities'] == apartment_data['facilities']