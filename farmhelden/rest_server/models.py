import jwt
from django.conf import settings
from django.contrib.gis.db import models as gisModels
from django.contrib.gis.forms import PointField
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from datetime import datetime, timedelta


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, email, password=None):
        """Create and return a `User` with an email and password."""
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    USER_CHOICES = (
        ('1', 'Landwirt'),
        ('2', 'Helfer'))

    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    point = gisModels.PointField(null=True)
    has_license = models.BooleanField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=32)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    point = gisModels.PointField(null=True)
    zip_code = models.CharField(max_length=16, null=True)
    street = models.CharField(max_length=128, null=True)


class Location(models.Model):
    LOCATION_TYPES = (('1', 'Bauernhof'), ('2', 'Treffpunkt'))
    id = models.AutoField(primary_key=True)
    point = PointField()
    info = models.TextField(max_length=1024)
    farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=1, choices=LOCATION_TYPES)


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    farm_id = models.ForeignKey(Farm, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()


class JobType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    needs_license = models.BooleanField()
    description = models.TextField(max_length=1024)


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    required_users = models.IntegerField()
    pending_jobs = models.ManyToManyField('PendingJob')


class PendingJob(models.Model):
    DECISION_TYPES = (('1', 'Pending'), ('2', 'Accepted'), ('3', 'Denied'))
    id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=DECISION_TYPES)
