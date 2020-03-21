from django.contrib.gis.db import models as gisModels
from django.contrib.gis.forms import PointField
from django.db import models


class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    USER_CHOICES = (
        ('1', 'Landwirt'),
        ('2', 'Helfer'))

    id = models.AutoField(primary_key=True)
    point = gisModels.PointField(null=True)
    has_license = models.BooleanField(null=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, null=True)


class Location(models.Model):
    LOCATION_TYPES = (('1', 'Bauernhof'), ('2', 'Feld'))
    id = models.AutoField(primary_key=True)
    point = PointField()
    info = models.TextField(max_length=1000)
    location_type = models.CharField(max_length=1, choices=LOCATION_TYPES)


class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    locations = models.ManyToOneRel(Location)
    point = gisModels.PointField(null=True)
    zip_code = models.CharField(max_length=10, null=True)
    street = models.CharField(max_length=100, null=True)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


class TaskType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    users = models.ManyToManyField(User)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, null=True, on_delete=models.SET_NULL)
    needs_license = models.BooleanField()
    users = models.ManyToManyField(User)
    description = models.TextField(max_length=1000)
