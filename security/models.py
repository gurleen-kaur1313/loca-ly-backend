from django.conf import settings
from django.db import models
import uuid


class PoliceEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    locality = models.CharField(null=True,blank=True,max_length=250)
    city = models.CharField(null=True,blank=True,max_length=250)
    state = models.CharField(null=True,blank=True,max_length=250)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(PoliceEmergency, self).save(*args, **kwargs)
