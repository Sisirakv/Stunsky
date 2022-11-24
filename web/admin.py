from django.contrib import admin

from .models import Blog, Testimonial, Category, Portfolio, Contact, Client

# Register your models here.

admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Client)