from django.db import models

class Result(models.Model):
    name = models.CharField(max_length=700, help_text="Keep in UPPERCASE")
    grade_class = models.CharField(max_length=100)
    gpa = models.CharField(max_length=4)
    password = models.CharField(max_length=100,help_text="Keep in UPPERCASE")
    remarks = models.TextField(blank=True)
    grade_sheet = models.FileField(upload_to='result/')

    def __str__(self):
        return self.name

