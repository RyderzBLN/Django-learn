from django.urls import path
from .views import startView, single_int_gadget, \
    GadgetView


urlpatterns = [
    path("", startView),
    path("gadget/", GadgetView.as_view()),
    path("gadget/<int:gadget_id>", single_int_gadget),
    path("gadget/<slug:gadget_slug>",
         GadgetView.as_view(), name="single_gadget_url"),

]
