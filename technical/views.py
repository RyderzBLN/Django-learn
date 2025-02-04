from django.shortcuts import render
from django.http import HttpResponse 
import json

from .dummyData import gadgets

# Create your views here.

def startView(request):
    return HttpResponse("HELLO WORLD")

def single_gadget(request):
    return HttpResponse(json.dumps(gadgets[0]))