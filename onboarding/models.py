from django.db import models
# from django.core.validators import MinLengthValidator

# Create your models here.


class OnboardingModel(models.Model):
    name = models.CharField(max_length=100)
    balance = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    network = models.CharField(max_length=100)
    address  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
