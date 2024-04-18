from django.shortcuts import render
from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'index.html'

class AboutView(views.TemplateView):
    template_name = 'core/about.html'

class FAQView(views.TemplateView):
    template_name = 'core/faq.html'
