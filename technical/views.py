from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.utils.text import slugify

from .dummyData import gadgets

# Create your views here.

def startView(request):
    return HttpResponse("HELLO WORLD")

def single_gadget(request,gadget_id):
    return JsonResponse({"result": slugify(gadgets[0]["name"])})