from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Blog, Testimonial, Portfolio, Category, Client

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(requset):
    testimonials = Testimonial.objects.all()
    client = Client.objects.all()[:12]
    
    ###Recent work###
    # category = Category.objects.filter(is_active = True)
    ui_ux = Portfolio.objects.filter(category__title="UI/UX").last()
    graphics_design = Portfolio.objects.filter(category__title="Graphics Design").last()
    packaging = Portfolio.objects.filter(category__title="Packaging").last()
    web_development = Portfolio.objects.filter(category__title="Web Development").last()
    other_offerings = Portfolio.objects.filter(category__title="Other offerings").last()
    print(ui_ux)
    context = {
        "testimonials":testimonials,
        "client":client,
        "ui_ux":ui_ux,
        "graphics_design":graphics_design,
        "packaging":packaging,
        "web_development":web_development,
        
        
        # "portfolio":portfolio
    }
    return render(requset, 'index.html', context)


def about_us(requset):
    client = Client.objects.all()[:12]
    context = {
        "client":client,
    }
    return render(requset, 'about-us.html', context)

@csrf_exempt
def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == "POST":
        print('hi')
        print(forms.errors) 
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
            
            
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context= {
            "is_contact" : True,
            "forms":forms,

        }
    return render(request,"contact.html",context)




def blog(request):
    blog_banner = Blog.objects.all()[:3]
    blog_list = Blog.objects.all() 
    print(blog_list)
    context = {
        
        "blog_banner":blog_banner,
        "blog_list" : blog_list,
    }
    return render(request,'blog.html',context)




def blog_details(request, id):
    blog = Blog.objects.get(id = id)  
    print(blog)
    context = {
        "is_blog" : True,
        "blog" : blog,
    }
    return render(request,"blog-single.html",context)


def portfolio(requset):
    category = Category.objects.filter(is_active = True)
    portfolio = Portfolio.objects.all()
    context = {
        "is_product" : True,
        "category" : category,
        "portfolio" : portfolio,
    }
    
    return render(requset, 'portfolio.html', context)


def careers(requset):
    return render(requset, 'Careers.html')


def careers_details(requset):
    return render(requset, 'Careers details.html')


def ui_ux(requset):
    # category = Category.objects.filter(is_active = True, title = "UI/ UX")
    portfolio = Portfolio.objects.filter(category__title = "UI/UX")
    context = {
        # "category":category,
        "portfolio":portfolio,
    }
    return render(requset, 'ui-ux.html', context)


def graphic_design(requset):
    portfolio = Portfolio.objects.filter(category__title = "Graphics Design")
    context = {
        # "category":category,
        "portfolio":portfolio,
    }
    return render(requset, 'graphic design.html', context)

def packaging(requset):
    portfolio = Portfolio.objects.filter(category__title = "Packaging")
    context = {

        "portfolio":portfolio,
    }
    return render(requset, 'packaging.html', context)


def web_development(requset):
    portfolio = Portfolio.objects.filter(category__title = "Web Development")
    context = {

        "portfolio":portfolio,
    }
    return render(requset, 'web development.html', context)


def other_offerings(requset):
    return render(requset, 'other offerings.html')


def design_digital_media(requset):
    return render(requset, 'design and digital media.html')

def image_data_services(requset):
    return render(requset, 'image and data services.html')