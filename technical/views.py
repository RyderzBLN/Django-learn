from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import json

from .dummyData import gadgets

# Create your views here.

def startView(request):
    return HttpResponse("HELLO WORLD")

def single_gadget(request,gadget_id):
    return JsonResponse({"test": gadget_id})