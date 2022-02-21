from email import message
from pyexpat import model
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=500)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    add1 = models.CharField(max_length=500)
    add2 = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.add1} {self.add2}"




