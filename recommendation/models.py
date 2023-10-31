from django.db import models
from django.contrib.auth.models import User

class Recommendation (models.Model):
    recommendationid = models.CharField(max_length=50)
    student = models.ForeignKey(User , on_delete=models.CASCADE)
 

# Create your models here.
