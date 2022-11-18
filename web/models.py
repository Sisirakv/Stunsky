from tabnanny import verbose
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify

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