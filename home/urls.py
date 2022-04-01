from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [
    path('', home, name='home'),
    path('about',about, name='about'),
    path('contact',contact, name='contact'),
    path('portfolio',portfolio, name='portfolio'),
    path('price',price, name='price'),
    path('services',services, name='services'),

    path('blog/',blog, name='blog'),
    path('blog/<str:id>',blog_single, name='blog-single'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)




