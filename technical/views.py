from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json
from django.views import View

from .dummyData import gadgets

# Create your views here.


def startView(request):
    return HttpResponse("HELLO WORLD")

class GadgetView(View):

    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                gadget_slug = gadget_slug

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f'POST data: {data}')
            return JsonResponse({"response": "Super geklappt / MURO"})
        except:
            return JsonResponse({"error": "Something went wrong / MURO"})




def single_int_gadget(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("single_gadget_url", args=[new_slug])

        return redirect(new_url)
    return HttpResponseNotFound("Gadget not found")


def single_gadget_view(request, gadget_slug=""):
    if request.method == "GET":
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                gadget_slug = gadget_slug

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f'POST data: {data}')
            return JsonResponse({"response": "Super geklappt / MURO"})
        except:
            return JsonResponse({"error": "Something went wrong / MURO"})




