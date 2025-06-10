from django.urls import path
from .views import  single_int_gadget, \
    GadgetView, RedirectToGadgetView


urlpatterns = [
    path("", RedirectToGadgetView.as_view()),
    path("<int:gadget_id>", RedirectToGadgetView.as_view()),
    path("gadget/", GadgetView.as_view()),
    path("gadget/<int:gadget_id>", single_int_gadget),
    path("gadget/<slug:gadget_slug>",
         GadgetView.as_view(), name="single_gadget_url")

]
