from email import message
from pyexpat import model
from django.db import models

STATUS = (('active','active'),('','default'))

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS = ('Publish','Publish'),('Draft','Draft')

    image = models.ImageField(upload_to = "Filter_Image/blog")
    additional_image = models.ImageField(upload_to = "Filter_Image/blog",blank=True,null=True)
    additional_image1 = models.ImageField(upload_to = "Filter_Image/blog",blank=True,null=True)
    title = models.CharField(max_length=300)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    description4 = models.TextField()
    description5 = models.TextField()
    description6 = models.TextField()
    status = models.CharField(choices=STATUS,max_length=200,null=True,blank=True)
     
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.title





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

class Filter_category(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS,blank=True, max_length=100)
    data_filter = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Content(models.Model):
    image = models.ImageField(upload_to = "Filter_Image/images")
    preview_image = models.ImageField(upload_to = "Filter_Image/images")
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    data_filter = models.CharField(max_length=200,null=True,blank=True)

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




