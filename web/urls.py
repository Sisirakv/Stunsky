
from django.urls import path
from . import views

urlpatterns = [

        path("", views.index, name="index"), 
        path("about us", views.about_us, name="about us"), 
        path("contact", views.contact, name="contact"),
        path("Blog", views.blog, name="Blog"),
        path("UI UX", views.ui_ux, name="UI UX"),
        path('portfolio', views.portfolio, name="portfolio"),
        path('careers', views.careers, name="careers")
        
]