from webbrowser import get
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Contact
from django.views import View

# Create your views here.


class ContactForm(View):
    def get(self, request):
        myform = Contact()
        return render(request, 'mainsite/contactme.html', {
            'form': myform,
        })

    def post(self, request):
        myform = Contact(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponseRedirect("/thanks")
        return render(request, 'mainsite/contactme.html', {
            'form': myform,
        })


def popup(request):
    return render(request, 'mainsite/popup.html')


def index(request):
    return render(request, 'mainsite/index.html')


# def contact_me(request):
#     if request.method == 'POST':
#         myform = Contact(request.POST)
#         if myform.is_valid():
#             myform.save()
#             return HttpResponseRedirect("/thanks")
#     else:
#         myform = Contact()
#     return render(request, 'mainsite/contactme.html', {
#         'form': myform,
#     })


def submitform(request):
    return render(request, 'mainsite/thanks.html')
