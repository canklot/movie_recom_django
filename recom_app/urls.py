from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("onerial", views.onerial, name="onerial"),
    path("filmler", views.filmler, name="filmler"),
    path("printLikes", views.printLikes, name="printLikes"),
]