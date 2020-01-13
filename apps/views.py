from django.shortcuts import render,redirect
from wakkanai import settings
from django.core.mail import send_mail
#from django.template.loader import get_template
#from django.utils.translation import gettext as _
from django.http import HttpResponse


# Create your views here.

def contact(request):

    print (request.method)
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        message = request.POST.get("subject")


        subject = message
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [email]

        send_mail(
            subject,message
            ,from_email,
            to_email, fail_silently=True)
        print (request)
        return redirect('go')
    return render(request, 'suru/contact.html',)


def go (request):
    return render(request, 'suru/go.html')





# def mail(request):
#     subject = "welcome to mail"
#     msg = "congratulation you got mail"
#     to = "bastolasujan09@gmail.com"
#     res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
#     if(res == 1):
#         msg = "mail sccessfuly"
#     else:
#         msg = "mail could not sent"
#     return HttpResponse(msg)
