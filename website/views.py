from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
# Create your views here.
def home(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        scheldule = request.POST['scheldule']
        time = request.POST['time']
        message = request.POST['message']
        try:
            ins = Appointment(name=name, phone=phone, email=email, address=address, scheldule=scheldule, time=time, message=message)
            ins.save()
            error = "no"
        except:
            error = "yes"

    context = {'error':error}
    return render(request, 'home.html', context)

def Contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_mail(
            message_name, #subject
            message, #message
            message_email, # from email
            ['15203023amitgoswami@gmail.com'], #to email
        )
        
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html')


def About(request):
    return render(request, 'about.html')

def Service(request):
    return render(request, 'service.html')

def Pricing(request):
    return render(request, 'pricing.html')

