from django.urls import path
from .views import startView, single_gadget, single_gadget_slug


urlpatterns = [
    path("", startView),
    path("gadget/<slug:gadget_slug>", single_gadget_slug)
]

