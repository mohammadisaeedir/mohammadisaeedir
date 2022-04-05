from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contactme/', views.ContactForm.as_view()),
    path('thanks/', views.SubmitView.as_view()),
    path('popup/', views.popup),
    path('contacts', views.Contacts.as_view()),
    # path('contacts/<int:id>', views.detailcontact, name='cont'),
    path('contacts/<int:pk>', views.DetailContact.as_view(), name='cont'),
]
