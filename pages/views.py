from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class BlogView(TemplateView):
    template_name = 'pages/blog.html'
