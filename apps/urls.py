from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.contact, name='contact'),
    path('go', views.go, name='go'),
    path('mail', views.mail, name='mail'),
    ]
