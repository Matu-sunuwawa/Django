from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# def index(request):
	
#     if request.method == 'POST':
#         message = request.POST['message']
        
#         send_mail('Contact Form',
#         message,
#         settings.EMAIL_HOST_USER,
#         ['matthiassinalemesa@gmail.com'],
#         fail_silently=False)
#     return render(request, 'app/index.html')

def index(request,):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
    return render(request, 'app/index.html')