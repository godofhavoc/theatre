# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=256)
    auditoriums = models.ManyToManyField('Auditorium')

    def __str__(self):
        return self.name

class Auditorium(models.Model):
    name = models.CharField(max_length=256)
    seats = models.ManyToManyField('Seat')

    def __str__(self):
        return self.name

class Seat(models.Model):
    row = models.PositiveSmallIntegerField()
    position = models.PositiveIntegerField()
    booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.row) + ' ' + str(self.position)
