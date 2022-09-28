from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    template = loader.get_template('mysite/home.html')
    context = {}

    return HttpResponse(template.render(context, request))