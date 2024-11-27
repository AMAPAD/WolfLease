'''
Copyright 2023 Ashwattha Phatak, Anish Mulay, Akshay Dongare

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserLogin, UserLogout

router = DefaultRouter()
router.register(r'flats', views.FlatViewSet, basename='flat')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'leases', views.LeaseViewSet, basename='lease')
router.register(r'interests', views.InterestViewSet, basename='interest')
router.register(r'apartments', views.ApartmentViewSet, basename='apartment')

urlpatterns = [
    path('', include(router.urls)),
    # path('owners', views.OwnerViewSet.as_view()),
    # path('owners/<str:pk>', views.OwnerViewSet.as_view()),
    # path('flats', views.FlatViewSet.as_view()),
    # path('flats/<str:pk>', views.FlatViewSet.as_view()),
    # path('lease', views.LeaseViewSet.as_view()),
    # path('lease/<str:pk>', views.LeaseViewSet.as_view()),
    # path('interests', views.InterestedViewSet.as_view()),
    # path('interests/<str:pk>', views.InterestedViewSet.as_view()),
    # path('apartments', views.ApartmentViewSet.as_view()),
    # path('apartments/<str:pk>', views.ApartmentViewSet.as_view()),
    # path('users', views.UserViewSet.as_view()),
    # path('users/<str:pk>', views.UserViewSet.as_view()),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('sign/<str:lease_identifier>/<str:username>/<str:dob>', views.sign_lease, name='sign_lease'),
]
'''Rest API endpoints'''