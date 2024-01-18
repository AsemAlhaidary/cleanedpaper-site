from django.shortcuts import render
from django.views.generic.base import TemplateView
from pages.settings import DEFAULT_SETTINGS, THEME_SETTINGS


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["theme"] = THEME_SETTINGS
        context["site"] = DEFAULT_SETTINGS
        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["theme"] = THEME_SETTINGS
        context["site"] = DEFAULT_SETTINGS
        return context


class BlogView(TemplateView):
    template_name = 'pages/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["theme"] = THEME_SETTINGS
        context["site"] = DEFAULT_SETTINGS
        return context
