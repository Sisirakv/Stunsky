from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("about us", views.about_us, name="about us"),
    path("contact", views.contact, name="contact"),
    path("Blog/", views.blog, name="Blog"),
    path("Blog Details/<int:id>", views.blog_details, name="Blog Details"),
    path("UI UX", views.ui_ux, name="UI UX"),
    path("Graphic Design", views.graphic_design, name="Graphic Design"),
    path("Package Design", views.packaging, name="Package Design"),
    path("Web Development", views.web_development, name="Web Development"),
    path("other offerings", views.other_offerings, name="other offerings"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("careers", views.careers, name="careers"),
    path("careers_details/<int:id>", views.careers_details, name="careers_details"),
    path("design & digital media", views.design_digital_media, name="design & digital media"),
    path("image & data services", views.image_data_services, name="image & data services"),
    path("data-processing-services", views.data_processing_service, name="data-processing-services"),
]
