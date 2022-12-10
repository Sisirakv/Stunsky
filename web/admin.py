from .models import ApplyNow
from .models import Blog
from .models import Category
from .models import CategoryDigitalMedia
from .models import Client
from .models import Contact
from .models import DesignDigitalMedia
from .models import ImgageDataService
from .models import JobDetails
from .models import Portfolio
from .models import Team
from .models import Testimonial
from .models import DataProcessingService
from django.contrib import admin



admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(JobDetails)
admin.site.register(ApplyNow)
admin.site.register(Team)
admin.site.register(CategoryDigitalMedia)
admin.site.register(DesignDigitalMedia)
admin.site.register(ImgageDataService)
admin.site.register(DataProcessingService)
