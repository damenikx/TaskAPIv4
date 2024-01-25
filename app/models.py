from django.db import models


class Office(models.Model):
    address = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return self.address


class Room(models.Model):
    officeID = models.ForeignKey(Office, related_name='offices', on_delete=models.CASCADE)
    room_number = models.IntegerField()
    floor = models.IntegerField()


class Point(models.Model):
    roomID = models.ForeignKey(Room, related_name='rooms', on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_reservation = models.BooleanField()


class Reservation(models.Model):
    pointID = models.ForeignKey(Point, related_name='points', on_delete=models.CASCADE)
    reservation_from = models.DateTimeField()
    reservation_to = models.DateTimeField()
