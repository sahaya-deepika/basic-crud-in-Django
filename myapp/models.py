from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    symptoms = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    admitted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
