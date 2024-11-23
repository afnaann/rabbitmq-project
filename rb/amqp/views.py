from django.shortcuts import render
from django.http import HttpResponse

from .rabbitmq import publish_message
# Create your views here.

def index(request):
    
    publish_message('This is Going to be in the queue')
    
    return HttpResponse('This is the rabbitMq Queue Going!')