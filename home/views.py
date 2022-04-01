from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def home(request):
    views = {}
    views['feedback'] = Feedback.objects.all()
    views['filter_category'] = Filter_category.objects.all()
    views['content'] = Content.objects.all()
    return render(request,'index.html',views)

    
def about(request):
    return render(request,'about.html')

# for send email
from django.core.mail import EmailMessage
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject= subject,
            message = message
        )
        data.save()

        email = EmailMessage(
            'Hello',
            'Hello thanks for the messagin us. We will get follow back to you!',
            'ef1b77d2319026',
            [email],
        )
        email.send()
        messages.success(request,'Email has been sent!')
        return redirect('home:home')
    views = {}
    views['infos'] = Information.objects.all()

    return render(request,'contact.html',views)



def blog(request):
    category = Categories.objects.all()
    blog = Blog.objects.all()
    

    categoriesID = request.GET.get('categories')

    if categoriesID:
        blog = Blog.objects.filter(category = categoriesID)
    else:
        blog = Blog.objects.filter(status = 'Publish').order_by('-id')

    context = {
        "category":category,
        "blog":blog,
    }
    return render(request,'blog-home.html',context)

def blog_single(request,id):
    category = Categories.objects.all()
    blog = Blog.objects.filter(id=id).first()

    context = {
        "category":category,
        "blog":blog,
    }
    return render(request,'blog-single.html',context)



def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')

    








