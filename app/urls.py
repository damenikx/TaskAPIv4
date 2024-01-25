from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('offices/', OfficeAPIList.as_view()),
    path('offices/<int:pk>/', OfficeAPIUpdateDestroy.as_view()),
    path('rooms/', RoomAPIList.as_view()),
    path('rooms/<int:pk>/', RoomAPIUpdateDestroy.as_view()),
    path('reservations/', ReservationAPIList.as_view()),
    path('reservations/<int:pk>/', ReservationAPIUpdateDestroy.as_view()),
    path('points/', PointAPIList.as_view()),
    path('points/<int:pk>/', PointAPIUpdateDestroy.as_view()),
]
