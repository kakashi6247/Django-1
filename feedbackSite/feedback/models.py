from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class users(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)