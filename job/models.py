from django.conf import settings
from django.db import models
import uuid

class Jobs(models.Model):
    WORK_CHOICES = (
        ("Y", "YES"),
        ("N", "NO"),
    )
    JOBTYPE_CHOICES = (
        ("P", "Part time"),
        ("F", "Full time"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    title = models.CharField(blank=True, max_length=250,null=False)
    description = models.TextField(null=True,blank=True)
    pay = models.IntegerField(null=True,blank=True)
    skillsrequired = models.TextField(null=True,blank=True)
    minimumdesignation = models.TextField(null=True,blank=True)
    mobile=models.CharField(blank=True,null=True,max_length=16)
    location=models.CharField(blank=True,null=True,max_length=250)
    jobtype = models.CharField(
        max_length=250, choices=JOBTYPE_CHOICES, blank=True, null=True
    )
    workfromhome = models.CharField(
        max_length=250, choices=WORK_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Jobs, self).save(*args, **kwargs)
