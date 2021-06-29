from django.db import models

class Info(models.Model):
    GENDER_CHOICES = (
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Other' , 'Other'),
    )
    student_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    Dob = models.DateField()
    contact_number = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    email_field = models.EmailField() 
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    school = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    tenth_cgpa = models.FloatField()
    twelth_perc = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mentor_name = models.CharField(max_length=100)
    stipend = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.student_name


# Create your models here.
