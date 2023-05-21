from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("onerial", views.onerial, name="onerial"),
    path("filmler", views.filmler, name="filmler"),
    path("results", views.results, name="results"),
    path("results_mock", views.results_mock, name="results_mock"),
    path("printLikes", views.printLikes, name="printLikes"),
]