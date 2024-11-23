'''
    This is the database strcuture of the models.
    Create your models here.

'''

from enum import unique
from django.db import models
import uuid

class User(models.Model):
    """
    This is User database structure.
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    '''Autogenerated Primary ID of User'''
    # flat_id = models.ForeignKey(to=Flat,null=True, blank=True, on_delete=models.SET_NULL)
    '''Flat ID of User'''
    USER_TYPE_CHOICES = [
        ('User', 'User'),
        ('Owner', 'Owner'),
    ]
    contact_number = models.CharField(max_length=12)
    '''Contact number of User'''
    contact_email = models.EmailField(max_length=30)
    '''Contact email of User'''
    password = models.CharField(max_length=50)
    '''Password of User'''
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='User'
    )
    '''Type of User'''
    dob = models.DateField()
    '''Date of Birth of User'''
    gender = models.CharField(default="M", max_length=2)
    '''Gender of User'''
    pref_smoking = models.CharField(default="N", max_length=2)
    '''Smoking preference of User'''
    pref_drinking = models.CharField(default="N", max_length=2)
    '''Drinking preference of User'''
    pref_veg = models.CharField(default="N", max_length=2)
    '''Vegetarian preference of User'''
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100, editable=True)

    def __str__(self):
        """
        This is used for login using email.
        """
        return self.username



# class Owner(models.Model):
#     """
#     This is a Owner database structure.
#     """
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     ) 
#     '''Autogenerated Primary ID of Owner'''
#     contact_number = models.CharField(max_length=12)
#     '''Contact number of Owner''' 
#     contact_email = models.EmailField(unique=True ,max_length=30)
#     '''Contact email of Owner'''
#     password = models.CharField(max_length=50)
#     '''Password of Owner'''
#     name = models.CharField(max_length=100)
#     '''Name of the Owner'''


class Apartment(models.Model):
    """
    This is Apartment database structure.
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    '''Autogenerated Primary ID of Apartment'''
    address = models.CharField(max_length=256)
    '''Address of Apartment'''
    facilities = models.CharField(max_length=512)
    '''Facilities of Apartment'''
    # owner_id = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    '''Owner ID of respective Apartment'''
    owner_id = models.ForeignKey(to=User, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    '''Name of the Appartment'''
    
    def __str__(self):
        return self.name

class Flat(models.Model):
    """
    This is Flat database structure.
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    '''Autogenerated Primary ID of Flat'''
    availability = models.BooleanField(default=False)
    '''Availibility of Flat'''
    # associated_apt_id = models.ForeignKey(to=Apartment, on_delete=models.DO_NOTHING)
    # '''Associated ID of respective Flat'''
    # lease_id = models.ForeignKey(to=Lease, on_delete=models.DO_NOTHING)
    '''Lease ID of respective Flat'''
    associated_apt_name = models.ForeignKey(to=Apartment, on_delete=models.DO_NOTHING)
    # lease_id = models.ForeignKey(to=Lease, null=True, on_delete=models.SET_NULL)
    rent_per_room = models.IntegerField()
    '''Rent per room of Flat'''
    floor_number = models.IntegerField()
    '''Floor number of Flat'''
    flat_number = models.IntegerField()
    '''Flat number'''
    # flat_identifier = associated_apt_name + "_" + floor_number + "_" + flat_number
    # '''Unique identifier for the flat combining apartment name and floor number'''
    flat_identifier = models.CharField(max_length=255, editable=False, primary_key=True, unique=True)

    ownername = models.ForeignKey(to=User, null=True, on_delete=models.DO_NOTHING)
    
    def save(self, *args, **kwargs):
        if self.associated_apt_name:
            self.flat_identifier = f"{self.associated_apt_name}_{self.floor_number}_{self.flat_number}"
        else:
            self.flat_identifier = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.flat_identifier


class Interested(models.Model):
    """
    This is Interested database structure.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    apartment_name = models.ForeignKey(to=Apartment, on_delete=models.DO_NOTHING)
    '''Generated ID of respective Apartment'''
    flat_identifier = models.ForeignKey(to=Flat, on_delete=models.DO_NOTHING)
    '''Flat ID of respective Flat'''
    username = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    '''User ID of respective User'''



class Lease(models.Model):

    """
    This is Lease database structure.
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    '''Autogenerated Primary ID of Lease'''
    lease_start_date = models.DateField()
    '''Start of lease date'''
    lease_end_date = models.DateField()
    '''End of lease date'''
    flat_identifier = models.ForeignKey(to=Flat, on_delete=models.DO_NOTHING)
    tenant_name = models.CharField(max_length=100)
    ownername = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    lease_identifier = models.CharField(max_length=200, primary_key=True, unique=True, default=None)
    is_signed = models.BooleanField(default=False)
    def __str__(self):
        return self.lease_identifier
    

class Review(models.Model):
    """
    This is the Review database structure.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    '''Autogenerated Primary ID of Review'''
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, related_name="reviews")
    '''Flat being reviewed'''
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_reviews")
    '''User who wrote the review'''
    rating = models.PositiveSmallIntegerField()
    '''Rating given by the user (1-5)'''
    comment = models.TextField(max_length=512, blank=True, null=True)
    '''Optional review comment'''
    created_at = models.DateTimeField(auto_now_add=True)
    '''Timestamp when the review was created'''

    def __str__(self):
        return f"Review by {self.user.username} for {self.flat.flat_identifier}"
