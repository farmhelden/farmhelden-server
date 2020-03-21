from django.db import models


class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    zip_code = models.CharField(max_length=10)
    has_license = models.BooleanField(null=True)
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL)


class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=30, null=True, blank=True)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    needs_license = models.BooleanField()
    users = models.ManyToManyField(User)


class TaskType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)



