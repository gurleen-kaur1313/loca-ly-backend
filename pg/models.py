from django.conf import settings
from django.db import models
import uuid


class Pgs(models.Model):
    USERTYPE_CHOICES = (
        ("B", "BOYS"),
        ("G", "GIRLS"),
        ("O", "BOTH"),
    )
    ROOMTYPE_CHOICES = (
        ("1", "SINGLE SEATER"),
        ("2", "DOUBLE SEATER"),
        ("3", "THREE SEATER"),
    )
    KITCHEN_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),
    )
    WASHROOM_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),
    )
    LAUNDRY_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    usertype = models.CharField(
        max_length=250, choices=USERTYPE_CHOICES, blank=True, null=True
    )
    roomtype = models.CharField(
        max_length=250, choices=ROOMTYPE_CHOICES, blank=True, null=True
    )
    kitchen_available = models.CharField(
        max_length=250, choices=KITCHEN_CHOICES, blank=True, null=True
    )
    washroom_attached = models.CharField(
        max_length=250, choices=WASHROOM_CHOICES, blank=True, null=True
    )
    laundry_included = models.CharField(
        max_length=250, choices=LAUNDRY_CHOICES, blank=True, null=True
    )
    rent = models.IntegerField(null=True,blank=True)
    locality = models.CharField(null=True,blank=True,max_length=250)
    city = models.CharField(null=True,blank=True,max_length=250)
    state = models.CharField(null=True,blank=True,max_length=250)
    url = models.URLField(null=True, blank=True,max_length = 200) 

    def __str__(self):
        return self.locality

    def save(self, *args, **kwargs):
        super(Pgs, self).save(*args, **kwargs)




