from django.db import models
class Member(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)


# Create your models here.
