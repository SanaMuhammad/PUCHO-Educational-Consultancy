from django.db import models
from django.contrib.auth.models import User

 
choices = (('F','Female'),('M','Male'))
uni_choices = (('University of Engineering and Technology','University of Engineering and Technology'),('Government College University Lahore','Government College University Lahore'),('Lahore College for Women University','Lahore College for Women University'),('Information Technology University','Information Technology University'),('Kinnard College For Women University','Kinnard College For Women University'),('University of Education','University of Education'))
dept_choices = (('SE','SE'),('IT','IT'),('CE','CE'),('CS','CS'),('A','A'),('AED','AED'),('CRP','CRP'),('EER','EER'),('CE','CE'),('IME','IME'),('ME','ME'),('MCE','MCE'),('MINE','MINE'),('MME','MME'),('PGE','PGE'),('PID','PID'),('PPE','PPE'),('TEM','TEM'),('CHE','CHE'))
class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=15,choices=choices,default="Male")
    age = models.IntegerField()
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    gaurdian_name = models.CharField(max_length=50)
    gaurdian_income = models.IntegerField()
    name_of_school = models.CharField(max_length=50)
    matric_marks = models.IntegerField()
    year_of_matric = models.IntegerField()
    matric_grade = models.CharField(max_length=10)
    matric_board = models.CharField(max_length=50)
    name_of_college = models.CharField(max_length=50)
    inter_marks = models.IntegerField()
    year_of_inter = models.IntegerField()
    inter_grade = models.CharField(max_length=10)
    inter_board = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50,choices=uni_choices,default="University of Engineering and Technology")
    field_of_interest = models.CharField(max_length=50,choices=dept_choices,default="SE")
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)
# Create your models here.
