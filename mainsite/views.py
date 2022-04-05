from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Contact
from django.views import View
from django.views.generic.base import TemplateView
from .models import ContactForm as cf
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.

# old way
#  def contact_me(request):
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

# new way based on view model
# class ContactForm(View):
#     def get(self, request):
#         myform = Contact()
#         return render(request, 'mainsite/contactme.html', {
#             'form': myform,
#         })

#     def post(self, request):
#         myform = Contact(request.POST)
#         if myform.is_valid():
#             myform.save()
#             return HttpResponseRedirect("/thanks")
#         return render(request, 'mainsite/contactme.html', {
#             'form': myform,
#         })


# newest way based on formmodel
# class ContactForm(FormView):
#     template_name = 'mainsite/contactme.html'
#     form_class = Contact
#     success_url = '/thanks'

#     def form_valid(self, form):
#         form.save() # for save post data form
#         return super().form_valid(form)


# newest2 way based on createview
class ContactForm(CreateView):
    model = cf
    form_class = Contact
    # we can even dont use form if we dont need label and errormsg
    # we can use fields and excludes even here like forms.py
    template_name = 'mainsite/contactme.html'
    success_url = '/thanks'
    # this will be automatically save in db


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


# class Contacts(TemplateView):
#     template_name = 'mainsite/contacts.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         contcats = cf.objects.all()
#         context["contacts"] = contcats
#         return context

class Contacts(ListView):
    template_name = 'mainsite/contacts.html'
    model = cf

    context_object_name = 'contacts'


class DetailContact(DetailView):
    template_name = 'mainsite/cont.html'
    model = cf

# def detailcontact(request, id):
#      obj = cf.objects.get(pk=id)
#      return render(request, 'mainsite/cont.html', {
#           'detail': obj
#      })
