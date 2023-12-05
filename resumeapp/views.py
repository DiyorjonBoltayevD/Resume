from django.shortcuts import render
from django.views.generic import ListView

from resumeapp.forms import ContactForm
from resumeapp.models import *


# class AboutView(ListView):
#     model = AboutModel
#     context_object_name = 'about'
#     template_name = 'index.html'
#
#
# class ResumeView(ListView):
#     model = ResumeModel
#     context_object_name = 'resume'
#     template_name = 'index.html'
#
#
# class ContactView(ListView):
#     model = ContactModel
#     template_name = 'index.html'

def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    about = AboutModel.objects.all()
    resume = ResumeModel.objects.all()
    servis = ServisModel.objects.all()
    skills = Myskills.objects.all()
    ourprojects = OurProjects.objects.all()
    ourblog = Ourblog.objects.all()
    contact = ContactModel.objects.all()
    ctx = {
        'form': form,
        'about': about,
        'resume1': resume[:3],
        'resume2': resume[3:6],
        'servis': servis,
        'skills': skills,
        'projects1': ourprojects[:3],
        'projects2': ourprojects[3:6],
        'ourblog': ourblog,
        'contact': contact,

    }
    return render(request, 'index.html', ctx)
