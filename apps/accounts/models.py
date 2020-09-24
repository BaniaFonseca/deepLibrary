from django.db import models
from django.contrib.auth.models import AbstractUser

from bson.objectid import ObjectId

class User(AbstractUser):
    id = models.CharField(max_length=24, 
                        blank=False, 
                        default = str(ObjectId()),  
                        primary_key=True)