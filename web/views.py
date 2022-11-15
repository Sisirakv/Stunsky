from django.shortcuts import render

# Create your views here.


def index(requset):
    return render(requset, 'index.html')


def about_us(requset):
    return render(requset, 'about-us.html')


def contact(requset):
    return render(requset, 'contact.html')


def blog(requset):
    return render(requset, 'blog.html')

def ui_ux(requset):
    return render(requset, 'ui-ux.html')
