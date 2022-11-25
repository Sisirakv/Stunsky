from django.contrib import admin

from .models import Blog, Testimonial, Category, Portfolio, Contact, Client, JobDetails, ApplyNow, Team

# Register your models here.

admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(JobDetails)
admin.site.register(ApplyNow)
admin.site.register(Team)