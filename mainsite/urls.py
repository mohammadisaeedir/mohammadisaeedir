from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contactme/', views.ContactForm.as_view()),
    path('thanks/', views.submitform),
    path('popup/', views.popup),
]
