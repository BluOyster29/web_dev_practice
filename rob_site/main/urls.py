from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about",views.about, name="about"),
    #path("nils", views.nils, name="nils"),
    path("rob", views.rob, name="rob"),
    path("nils", views.rob, name="nils"),
]

