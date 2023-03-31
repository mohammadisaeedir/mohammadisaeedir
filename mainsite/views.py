from .models import *
from .forms import Contact
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpRes

# old way
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
    # try:
    #     send_mail(subject="New Contact form", message="saeed", from_email='sm1988ir@gmail.com', recipient_list=['mohammadisaeedir@gmail.com'])
    # except BadHeaderError:
    #     return HttpResponse('Bad Header Request')
    

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
class CF(CreateView):
    model = ContactForm
    form_class = Contact
    # we can even dont use form if we dont need label and errormsg
    # we can use fields and excludes even here like forms.py
    template_name = 'mainsite/contactme.html'
    success_url = '/thanks'
    # this will be automatically save in db



class MainPage(TemplateView):
    template_name = 'mainsite/mainpage.html'
    context_object_name = 'home_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = Options.objects.get(pk=1)
        context['social_network'] = ContactInfo.objects.filter(
            contact_type='sn')
        context['at_glance'] = ContactInfo.objects.filter(
            contact_type='glance')
        context['skills'] = SkillCategory.objects.all()
        context['experience'] = Experience.objects.all()
        context['positions'] = Experience.positions()
        context['education'] = Education.objects.all()
        context['certificate'] = Certificate.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['phone'] = ContactInfo.objects.filter(contact_type='phone')[0]
        context['mail'] = ContactInfo.objects.filter(contact_type='mail')[0]
        context['others'] = ContactInfo.objects.filter(contact_type='others')[0]
        return context


# class SubmitView(View):
#     def get(self, request):
#         return render(request, 'mainsite/thanks.html')

class SubmitView(TemplateView):
    template_name = 'mainsite/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body'] = 'We will be in touch'
        context['social_network'] = ContactInfo.objects.filter(
            contact_type='sn')
        return context


# class DetailContact(DetailView):
#     template_name = 'mainsite/cont.html'
#     model = ContactForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         favorite_id = self.request.session.get('favorite_contact')
#         if favorite_id == str(self.object.id):
#             context['is_favorite'] = True
#         return context


# class AddFavorite(View):
#     def post(self, request):
#         cont_id = request.POST['cont-id']
#         # fav_cont = cf.objects.get(pk=cont_id)
#         request.session['favorite_contact'] = cont_id
#         return HttpResponseRedirect('/contacts/' + cont_id)


# def popup(request):
#     return render(request, 'mainsite/popup.html')
