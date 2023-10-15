from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    context = {
        'variable1' : "'Vedansh, the great'",
        'variable2' : "'Vedansh is hot 🥵'"
    }
    return render(request,'index.html',context)

# Here, context is basically a dictionary containing a set of variables which is passed to 'render'.

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc= request.POST.get("desc")

        # Creating an object of the model "contact" and saving it...
        cont = contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        cont.save()
        messages.success(request, "The details have been submitted sucessfully.")
    return render(request,'contacts.html')