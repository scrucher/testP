import json
import urllib

from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def contactView(request):
    form = ContactForm()
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if name and phone and message and from_email:
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            try:
                send_mail(from_email, name, phone, message, ["jhonsteph666@gmail.com"],  )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent')
        else:
            messages.error(request, 'Invalid reCAPTCH. Please Try Again ')
    return render(request, "captcha/index.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')