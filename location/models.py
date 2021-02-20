from django.db import models

class Location(models.Model):
    city = models.CharField(null=True,blank=True,max_length=250)
    state = models.CharField(null=True,blank=True,max_length=250)
    rating = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.city

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)

