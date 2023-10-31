from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    Feedback_text = models.CharField(max_length=1000, default="")

    def __str__(self):
        return str(self.name)
