from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about",views.about, name="about"),
    #path("nils", views.nils, name="nils"),
    path("rob", views.rob, name="rob"),
    path("nils", views.nils, name="nils"),
    path("register", views.register, name="register"),
    path("nils_song", views.nilsong, name="nils_song"),
    path("rob_song", views.robsong, name="rob_song"),



]

