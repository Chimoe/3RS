import uuid
from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.building) + ": " + self.name

    def is_reserved(self):
        return self.reserved


