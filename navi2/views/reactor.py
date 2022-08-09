from django.shortcuts import render
from django.views.generic import TemplateView

# Fixe?
from navi2.live import TestComponent

class ReactorView(TemplateView):
    template_name = "reactor.html"
