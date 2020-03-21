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
    point = PointField()
    has_license = models.BooleanField(null=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, null=True)


class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    point = PointField()
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


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, null=True, on_delete=models.SET_NULL)
    needs_license = models.BooleanField()
    users = models.ManyToManyField(User)
    description = models.TextField(max_length=1000)
