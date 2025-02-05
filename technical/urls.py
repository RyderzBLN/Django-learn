from django.urls import path
from .views import startView, single_gadget, single_gadget_slug


urlpatterns = [
    path("", startView),
   path("gadget/<int:gadget_id>", single_gadget),
    path("gadget/<slug:gadget_slug>", single_gadget_slug, name="single_gadget_url"),
]

