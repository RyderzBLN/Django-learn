from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.utils.text import slugify

from .dummyData import gadgets

# Create your views here.

def startView(request):
    return HttpResponse("HELLO WORLD")

def single_gadget(request,gadget_id):
    return JsonResponse({"result": slugify(gadgets[0]["name"])})

def single_gadget_slug(request, gadget_slug):
    gadget_match = {"result": "nothing"}
    gadget_slug = gadget_slug.lower()

    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
    
      
    return JsonResponse(gadget_match)