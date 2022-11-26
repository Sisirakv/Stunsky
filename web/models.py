from tabnanny import verbose
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.

class Blog(models.Model):
    image = VersatileImageField('Image',upload_to='images/blog/')
    heading = models.TextField()
    short_heading = models.TextField(max_length=50)
    category = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True,editable=False)
    content = models.TextField()

    def __str__(self):
        return self.short_heading

    class Meta:
        verbose_name_plural =("Blog")
        
        
# class Gallery(models.Model):
#     name = models.CharField(max_length=200)
#     image = VersatileImageField('Image',upload_to='images/testimagemodel/')

#     class Meta:
#         verbose_name_plural =("Gallery")

#     def __str__(self):
#         return self.name
    
    
class Testimonial(models.Model):
    image = VersatileImageField('Image',upload_to='images/testimagemodel/')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)  
    review = models.TextField()
        
    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.title)
    
    
class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    image = VersatileImageField('Image',upload_to='images/portfolio/')
    title = models.TextField(max_length=200)
    
    class Meta:
        verbose_name_plural = ("Portfolio")

    def __str__(self):
        return str(self.title)
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    project_goals = models.TextField()
    phone = models.CharField(max_length=12)
    budeget = models.CharField(max_length=50)
    # message = models.TextField()

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/Client/')

    def __str__(self):
        return self.name
    
# career


class JobDetails(models.Model):
    job_title = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    salary = models.CharField(max_length=50, null=True, blank=True)
    vaccancy = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    job_description = HTMLField(null=True, blank=True)
    job_responsibility = HTMLField(null=True, blank=True)
    educational_requirments = HTMLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Jobs")

    def __str__(self):
        return str(self.job_title)
    
class ApplyNow(models.Model):
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE, null=True, blank=True)
    applicant_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    cv = models.FileField(upload_to='cv', null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Applications")

    def __str__(self):
        return str(self.applicant_name)
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/team/')
   
    
class CategoryDigitalMedia(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Category Digital Media")

    def __str__(self):
        return str(self.title)


class DesignDigitalMedia(models.Model):
    media_category = models.ForeignKey(CategoryDigitalMedia, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/digitalmedia/')

    class Meta:
        verbose_name_plural = ("Digital Media")
        
    def __str__(self):
        return self.title
    
    
class ImgageDataService(models.Model):
    image = VersatileImageField('Image',upload_to='images/imagedataservice/')
    title = models.CharField(max_length=200)
    details = models.TextField()
    
    