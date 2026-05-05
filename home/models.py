from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contacts(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.TextField()
  link = models.TextField(null=True, blank=True)
  