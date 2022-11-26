from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import *

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(requset):
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()[:12]
    
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
        "clients":clients,
        "ui_ux":ui_ux,
        "graphics_design":graphics_design,
        "packaging":packaging,
        "web_development":web_development,
        "other_offerings":other_offerings,
        
        # "portfolio":portfolio
    }
    return render(requset, 'index.html', context)


def about_us(requset):
    client = Client.objects.all()[:12]
    team = Team.objects.all()
    context = {
        "client":client,
        "team":team,
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


def portfolio(request):
    category = Category.objects.filter(is_active = True)
    portfolio = Portfolio.objects.all()
    context = {
        "is_product" : True,
        "category" : category,
        "portfolio" : portfolio,
    }
    
    return render(request, 'portfolio.html', context)


def careers(request):
    jobs = JobDetails.objects.all().order_by()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        jobs = JobDetails.objects.all().filter(job_title__icontains=search_term)
        context = {
            "is_career": True,
            "jobs": jobs,
        }
        return render(request, "Careers.html", context)
    context = {
        "jobs":jobs,
    }
    return render(request, 'Careers.html', context)



def careers_details(request, id):
    job_details = JobDetails.objects.filter(id=id)
    
    # Apply for job
    Jobdetails = JobDetails.objects.get(id=id)
    if request.method == 'POST':
        applicant_name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        cv = request.FILES['cv']
        job = Jobdetails
        new_application = ApplyNow(applicant_name=applicant_name, phone=phone, email=email, cv=cv, job=job)
        new_application.save()
        
    context = {
        "job_details" :job_details,
        "Jobdetails": Jobdetails,
    }
    return render(request, 'Careers details.html', context)


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


def design_digital_media(request):
    category_digital_media = CategoryDigitalMedia.objects.filter(is_active = True)
    digital_media = DesignDigitalMedia.objects.all()
    context = {
        "is_product" : True,
        "category_digital_media" : category_digital_media,
        "digital_media" : digital_media,
    }
    return render(request, 'design and digital media.html',context)

def image_data_services(request):
    data_service = ImgageDataService.objects.all()
    context = {
        "data_service":data_service
    }
    return render(request, 'image and data services.html', context)