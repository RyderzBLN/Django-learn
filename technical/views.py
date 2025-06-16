from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from .models import Gadget_List


from django.urls import reverse
import json
from django.views import View

from .dummyData import gadgets
from .dummyData import gadget

# Create your views here.

def gadget_info_view(request):
    return JsonResponse({"gadget" : gadget})

def startView(request):
    return HttpResponse("HELLO WORLD")


class RedirectToGadgetView(RedirectView):
    pattern_name = "single_gadget_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 1)]["name"])
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)

@csrf_exempt 
def gadget_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Empfangene Daten:", data)  # Zum Debuggen

            new_gadget = Gadget_List.objects.create(
                name=data.get('name'),
                headquarters=data.get('headquarters'),
                founded=data.get('founded'),
                website=data.get('website'),
                description=data.get('description')
            )
            print(f"Neues Gadget gespeichert mit ID: {new_gadget.id}")  # Extra Debug

            return JsonResponse({'success': True, 'id': new_gadget.id})
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)

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




