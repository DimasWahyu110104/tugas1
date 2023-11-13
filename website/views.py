from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def brainware(request):
    template = loader.get_template('brainware.html')
    return HttpResponse(template.render())
def hardware(request):
    template = loader.get_template('hardware.html')
    return HttpResponse(template.render())
def software(request):
    template = loader.get_template('software.html')
    return HttpResponse(template.render())
def utama(request):
    template = loader.get_template('utama.html')
    return HttpResponse(template.render())

    