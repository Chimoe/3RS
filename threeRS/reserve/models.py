from django.db import models


class Building(models.Model):
    building_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.building_name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=200)
    reservations = models.IntegerField(default=0)

    def __str__(self):
        return self.room_number

    def is_reserved(self):
        return reservations >= 1

