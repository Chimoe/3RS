from django.db import models

class Building(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    roomNumber = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.roomNumber