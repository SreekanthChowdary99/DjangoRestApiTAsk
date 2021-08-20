from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator,MaxLengthValidator


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no= models.IntegerField(unique = True)
    Dob=models.DateField()

    def __str__(self):
        return str(self.name)

class StudentGrades(models.Model):
    grades = models.CharField('grades', max_length=1, validators=[MaxLengthValidator(1)])

    def __str__(self):
        return str(self.grades)

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks=models.IntegerField(null=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    studentgrade = models.ForeignKey(StudentGrades, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.student)

