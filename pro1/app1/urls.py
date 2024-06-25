from django.urls import path

from .views import *

urlpatterns = [
    path("av/",add_person,name= "add-person"),
    path("pl/",show_person,name="person-list"),
    path("pv/<pk>/",update_person,name="person-update")
]