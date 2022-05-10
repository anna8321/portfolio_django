from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.views.generic import ListView

from .models import Blog
from django.views.generic import View
from .forms import ContactForm
from .models import Contact


# from django.apps import apps
# Project = apps.get_model('project', 'Project')


class HomepageView(ListView):
    model = Blog
    html_template = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        return render(request, self.html_template, context)

    def post(self, request):
        context = {}
        context['form'] = ContactForm()
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        company = request.POST["company"]
        email = request.POST["email"]
        content = request.POST["content"]
        phone = request.POST["phone"]
        contact = Contact.objects.create(firstname=firstname, lastname=lastname,
                                         company=company, email=email,
                                         content=content, phone=phone)
        contact.save()
        return redirect('blog:blog-homepage')

class ContactUs(View):
    html_template = "contact.html"

    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        return render(request, self.html_template, context)

    def post(self, request):
        context = {}
        context['form'] = ContactForm()
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        company = request.POST["company"]
        email = request.POST["email"]
        content = request.POST["content"]
        phone = request.POST["phone"]
        contact = Contact.objects.create(firstname=firstname, lastname=lastname,
                                         company=company, email=email,
                                         content=content, phone=phone)
        contact.save()
        return redirect('blog:blog-homepage')
