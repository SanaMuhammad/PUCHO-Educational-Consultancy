from django.db import models
from django.contrib.auth.models import User
 
class University (models.Model):
    university_name = models.CharField(max_length=150, blank= True)
    program_name = models.CharField(max_length=150)
    program_abbreviation = models.CharField(max_length=15,blank=True)
    last_merit = models.CharField(max_length=1500)
    eligibilty_criteria = models.CharField(max_length=1500)
    fee_structure = models.IntegerField()
    
    def __str__(self):
            return self.university_name + " " + self.program_name



class SavedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_page = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100,blank=True,null=True,default=None)

    def __str__(self):
        return self.user.username + " " + self.item_page

class UniversitiesCount(models.Model):
    university_name = models.CharField(max_length=150)
    count = models.IntegerField()

    def __str__(self):
        return self.university_name + " " + str(self.count)
# Create your models here.
