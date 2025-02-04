from django.urls import path
from .views import startView, single_gadget


urlpatterns = [
    path("", startView),
    path("gadget/", single_gadget)
]

