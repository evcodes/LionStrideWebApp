from django.db import models

# Models for Data Analysis
class School(models.Model):
    school_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    student_enrollment = models.IntegerField()

    # String representation of the model
    def __str__(self):
        return self.school_name + ' capacity: ' + str(self.student_enrollment)

class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    grade_level = models.IntegerField()
    student_ID = models.IntegerField()