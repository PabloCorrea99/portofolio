from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from .forms import EmailForm
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.is_ajax and request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            context = {
                'name':name,
                'email':email,
                'subject':subject,
                'body':body
            }
            enviar_correo_usuario(context)
            
            return JsonResponse({
                'content': {
                    'message': 'Su mensaje ha sido enviado correctamente',
                }
            }, status=200)
    else:

        return render(request,'home/index.html')

def enviar_correo_usuario(context):
    html = render_to_string('home/email.html', context)
    send_mail('Nuevo Correo Portafolio',
    'Nuevo Correo Portafolio',
    'promocioncarnes@gmail.com',
    ['correa.pablo1999@gmail.com'],
    fail_silently=False,
    html_message= html
    )