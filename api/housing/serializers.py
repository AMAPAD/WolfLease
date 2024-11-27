'''
Copyright 2023 Ashwattha Phatak, Anish Mulay, Akshay Dongare

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from rest_framework import serializers
from housing import models
from rest_framework.authtoken.models import Token 
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):
    """
        This is UserSerializer for User model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.User 
        '''User model '''
        fields = '__all__'
        '''User field '''
    
    def create(self, validated_data):
        """
            This is create method to create the user using password.
        """
        validated_data['password'] = make_password(validated_data['password'])
        '''Password validation'''
        return super(UserSerializer, self).create(validated_data)

class FlatSerializer(serializers.ModelSerializer):
    """
        This is FlatSerializer for Flat model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Flat
        '''Flat model'''
        fields = '__all__'
        '''Flat fields'''

# class OwnerSerializer(serializers.ModelSerializer):
#     """
#         This is OwnerSerializer for Owner model.
#     """
#     class Meta:
#         """
#             This class contains fields to be serialized.
#         """
#         model = models.Owner
#         '''Owner model'''
#         fields = '__all__'
#         '''Owner fields'''

class InterestedSerializer(serializers.ModelSerializer):
    """
        This is InterestedSerializer for Interested model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Interested
        '''Interested model'''
        fields = '__all__'
        '''Interested fields'''


class LeaseSerializer(serializers.ModelSerializer):
    """
        This is LeaseSerializer for Lease model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Lease
        '''Lease model'''
        fields = '__all__'
        '''Lease fields'''

class ApartmentSerializer(serializers.ModelSerializer):
    """
        This is ApartmentSerializer for Apartment model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Apartment
        '''Apartment model'''
        fields = '__all__'
        '''Apartment fields'''
