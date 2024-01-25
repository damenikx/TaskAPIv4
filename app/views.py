from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Office, Room, Reservation, Point
from rest_framework.permissions import IsAdminUser
from .serializers import OfficeSerializer, RoomSerializer, ReservationSerializer, PointSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OfficeAPIList(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class OfficeAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class RoomAPIList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PointAPIList(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PointAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class ReservationAPIList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


