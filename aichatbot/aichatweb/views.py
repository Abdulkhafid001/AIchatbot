from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())
