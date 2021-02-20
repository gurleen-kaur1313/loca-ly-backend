from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import MinValueValidator
from django.conf import settings
import uuid
from location.models import Location


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Please enter email")
        User = self.model(email=email)
        User.set_password(password)
        User.save()
        return User

    def create_superuser(self, email, password, is_staff=True):
        User = self.create_user(email, password)
        User.is_staff = True
        User.is_superuser = True
        User.save()
        return User


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def GET_Email(self):
        return self.email


class Profile(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True, max_length=250)
    mobile = models.CharField(blank=True, null=True,max_length=16)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    Age = models.IntegerField(blank=True, validators=[
                              MinValueValidator(0)], null=True)
    Gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)