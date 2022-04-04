from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Contact
from django.views import View
from django.views.generic.base import TemplateView
from .models import ContactForm as cf

# Create your views here.

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


# class SubmitView(View):
#     def get(self, request):
#         return render(request, 'mainsite/thanks.html')

class SubmitView(TemplateView):
    template_name = 'mainsite/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body'] = 'we will be in touch'
        return context


class Contacts(TemplateView):
    template_name = 'mainsite/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contcats = cf.objects.all()
        context["contacts"] = contcats
        return context

def surl(request, id):
     obj = cf.objects.get(pk=id)
     return render(request, 'mainsite/cont.html', {
          'detail': obj
     })
