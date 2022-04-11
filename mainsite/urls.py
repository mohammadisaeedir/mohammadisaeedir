from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view()),
    path('contactme/', views.CF.as_view()),
    path('thanks/', views.SubmitView.as_view()),
]
