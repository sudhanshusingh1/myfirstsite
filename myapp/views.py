from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= {
        "variable1":"bhai is great",
        "variable2":"boi is great"
    }
    return render(request,'index.html', context )
    #return HttpResponse("This is a home page")

def about(request):
    return render(request,'about.html')
   # return HttpResponse("This is a about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is a services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact= Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request,'contact.html')
    #return HttpResponse("This is a contact page")

def chinese(request):
    return render(request,'chinese.html')