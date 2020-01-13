# sending-email-through-contact-forms
[[[
(#this is the comment in django so you dont need to write)
* = just for goodlooking for you guys dont write in your code..
]]]]

sending email through contact form using sengrid
 in this project i am doing the send mail function using sendrig email service .....
 as usell  first create one project 
 *django-admin python.py startproject projectname
 then create one app
 **django-admin python.py startapp appname 
 *create templates folder to set your templates.....
 if you have ststic file like :css img js then also create one folder to your project ...at that time you have to create static and assets 
 because one is for our understanding and another is for djagno...
 then set the tempaletes path in settings.py...(i have in setting.py )
 ..
 first you have to go to the sendride site and make your profile and copy the API from there and you have to set these file in setting.py agaian ..
 ----settings.py---
 SENDGRID_API_KEY = os.getenv('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')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'username of sendgrid'
EMAIL_HOST_PASSWORD = 'yourpassword of sendgrid'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'example@gmail.com'(this is also from your sendgrid account)
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'we got your message thanks for believing us'

then you have to go to urls.py of project and mentaion the url of your app llike:
-----project/urls.py---
*from django.contrib import admin
*from django.urls import path, include
*#from django import views(#this is the comment in django so you dont need to write)
*#from django.conf.urls import url,include


*urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('first.urls')),


in result this url goes to your app url then again we have to set many urls in app/url also 
here is the setting of my apps/urls.py(you have to create new python file name as urls.py inside your app)

--apps/urls.py-----

*from django.urls import path,include
*from .import views

*urlpatterns = [

    path('', views.contact, name='contact'),
    path('go', views.go, name='go'),
    path('mail', views.mail, name='mail'),
    ]
    
for example i have 3 link inside my app so i declared 3 path in apps/urls.py
for send mail you dont need to write all just write the first one thats it.

-----views.py-----
*from django.shortcuts import render,redirect
from wakkanai import settings
from django.core.mail import send_mail

def contact(request):

    print (request.method)
    if request.method == "POST":
    #getting all the feilds input from the user....
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
        return redirect('go')#redirect to another path if the mail is gone..
    return render(request, 'suru(inside templates folder name)/contact.html',)

....................thats all guys thank you .............
