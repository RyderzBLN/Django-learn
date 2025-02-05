from django.shortcuts import redirect
from django.http import HttpResponse , JsonResponse
from django.utils.text import slugify
from django.urls import reverse

from .dummyData import gadgets

# Create your views here.

def startView(request):
    return HttpResponse("HELLO WORLD")

def single_gadget(request,gadget_id):
    new_slug = slugify(gadgets[gadget_id]["name"])
    new_url = reverse("single_gadget_url", args=[new_slug])

    return redirect(new_url)

def single_gadget_slug(request, gadget_slug):
    gadget_match = {"result": "nothing"}
    print(f"Gesuchter Slug: {gadget_slug}")  # Debugging




    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
    
      
    return JsonResponse(gadget_match)