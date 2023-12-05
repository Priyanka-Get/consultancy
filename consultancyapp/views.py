from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name ="consultancyapp/index.html"

class project(TemplateView):
    template_name="consultancyapp/portfolio-details.html"
      